# Generated by Django 4.2.3 on 2023-07-18 09:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book_site', '0003_userrank_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userrank',
            options={'verbose_name': '職務', 'verbose_name_plural': '職務'},
        ),
        migrations.RemoveField(
            model_name='review',
            name='post_imgs',
        ),
        migrations.AddField(
            model_name='review',
            name='main_img',
            field=models.ImageField(null=True, upload_to='photos/', verbose_name='主要影像'),
        ),
        migrations.AddField(
            model_name='user',
            name='blood_type',
            field=models.IntegerField(choices=[(0, 'A'), (1, 'B'), (2, 'O'), (3, 'AB'), (4, '不詳')], default=4, verbose_name='血型'),
        ),
        migrations.AddField(
            model_name='user',
            name='work_id',
            field=models.IntegerField(default=0, help_text='必填', max_length=8, unique=True, verbose_name='員工編號'),
        ),
        migrations.AlterField(
            model_name='images',
            name='image',
            field=models.ImageField(help_text='必填', upload_to='photos/', verbose_name='貼文圖片'),
        ),
        migrations.AlterField(
            model_name='user',
            name='sex',
            field=models.IntegerField(choices=[(0, '男性'), (1, '女性'), (3, '未知')], default=0, verbose_name='性別'),
        ),
        migrations.CreateModel(
            name='UserAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(help_text='必填', max_length=254, verbose_name='email')),
                ('password', models.CharField(max_length=500)),
                ('worker', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='book_site.user')),
            ],
        ),
    ]
