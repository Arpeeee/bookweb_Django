from django.db import models

# from django.template.defaultfilters import slugify
from django.utils.text import slugify
from django.urls import reverse  # 我的理解是reverse把某個資料表中的某個葉面的真實網址回傳


# Create your models here.
class bookCategory(models.Model):
    # id = models.AutoField(primary_key=True)
    category = models.CharField(verbose_name="書籍類別", max_length=20, null=False)

    def __str__(self):
        return self.category

    class Meta:
        verbose_name = "書籍類別"
        verbose_name_plural = "書籍類別"


# class Post(models.Model):
#     title = models.CharField(max_length=100)
#     content = models.TextField(blank=True)
#     photo = models.URLField(blank=True)
#     location = models.CharField(max_length=100)
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.title,self.content,self.photo,self.location

#     class Meta:
#         verbose_name = ""


class writers(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    name = models.CharField(verbose_name="作者姓名", max_length=10, null=False)

    def __str__(self):
        return self.name

    @property
    def list(self):
        return {
            "id": self.id,
            "name": self.name,
        }

    class Meta:
        verbose_name = "作者列表"
        verbose_name_plural = "作者列表"


class images(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    image = models.ImageField(
        verbose_name="貼文圖片", help_text="必填", null=False, upload_to="photos/"
    )
    sort = models.SmallIntegerField(verbose_name="圖片排序")

    class Meta:
        verbose_name = "貼文圖庫"
        verbose_name_plural = "貼文圖庫"


# 文章主要欄位
class review(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    categorys = models.ForeignKey(
        bookCategory, related_name="review", blank=True, on_delete=models.PROTECT
    )  # , on_delete=models.PROTECT
    main_title = models.CharField(
        max_length=30, null=False, verbose_name="主標題", help_text="必填"
    )
    book_title = models.CharField(max_length=30, verbose_name="書名")
    main_img = models.ImageField(verbose_name="主要影像", null=True, upload_to="photos/")
    content = models.TextField(verbose_name="貼文內容")
    sour = models.SmallIntegerField(verbose_name="風味-酸", default=0)
    sweet = models.SmallIntegerField(verbose_name="風味-甜", default=0)
    bitter = models.SmallIntegerField(verbose_name="風味-苦", default=0)
    spicy = models.SmallIntegerField(verbose_name="風味-辣", default=0)
    salt = models.SmallIntegerField(verbose_name="風味-鹹", default=0)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    writer = models.ForeignKey(
        writers, null=False, help_text="必填", blank=True, on_delete=models.PROTECT
    )
    # post_imgs = models.ManyToManyField(images, blank=True, null=True, verbose_name="圖片")
    slug = models.SlugField(
        max_length=255, verbose_name="Slug", unique=True, blank=True
    )

    # def get_absolute_url(self):
    #     return reverse("review.url.detail", kwargs={"slug": self.slug})

    def __str__(self):
        return f"{self.id}_{self.main_title}"

    # # slug 可以增加在網址最後面，讓我們不用再urls那編寫一大堆
    def save(self, *args, **kwargs):
        if not self.slug:  # Only populate the slug if it's not already set
            self.slug = f"{self.main_title.replace('-', ' ')}-{self.book_title.replace('-', ' ')}"
        super().save(*args, **kwargs)

    @property
    def list(self):
        output = {
            "id": self.id,
            "categorys": str(self.categorys),
            "main_title": self.main_title,
            "book_title": self.book_title,
            "content ": self.content,
            "sour ": self.sour,
            "sweet ": self.sweet,
            "bitter ": self.bitter,
            "spicy ": self.spicy,
            "salt ": self.salt,
            "created_time": self.created_time,
            "updated_time": self.updated_time,
            "writer ": str(self.writer),
            #   "post_imgs ": str(self.post_imgs) ,
            "slug": self.slug,
        }
        return output

    class Meta:
        verbose_name = "雙周更貼文"
        verbose_name_plural = "雙周更貼文"


class UserAccount(models.Model):
    worker = models.ForeignKey(
        writers, blank=True, null=False, on_delete=models.CASCADE
    )
    email = models.EmailField(verbose_name="email", null=False, help_text="必填")
    password = models.CharField(max_length=500)

    def save(self, *args, **kwargs):
        from django.contrib.auth.hashers import make_password

        if self.password:  # Only populate the slug if it's not already set
            self.password = make_password(password=self.password)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "帳號管理"
        verbose_name_plural = "帳號管理"
