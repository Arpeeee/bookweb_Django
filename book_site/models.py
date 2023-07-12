from django.db import models

# Create your models here.
class bookCategory(models.Model):
    # id = models.AutoField(primary_key=True)
    category = models.CharField(verbose_name="書籍類別", max_length=20, null=False)

    # def __str__(self):
    #     return self.category
    class Meta:
        verbose_name = "書籍類別"
        verbose_name_plural = "書籍類別"

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    photo = models.URLField(blank=True)
    location = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)