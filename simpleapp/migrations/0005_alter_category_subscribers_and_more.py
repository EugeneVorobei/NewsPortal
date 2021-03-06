# Generated by Django 4.0.4 on 2022-05-21 12:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('simpleapp', '0004_alter_category_subscribers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='subscribers',
            field=models.ManyToManyField(related_name='subscribers', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date_comment',
            field=models.DateTimeField(auto_now_add=True, verbose_name='дата'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='simpleapp.post'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='rating_comment',
            field=models.IntegerField(default=0, verbose_name='рейтинг'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='text_comment',
            field=models.TextField(verbose_name='текст'),
        ),
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='дата создания'),
        ),
        migrations.AlterField(
            model_name='post',
            name='header_post',
            field=models.CharField(max_length=255, verbose_name='название'),
        ),
        migrations.AlterField(
            model_name='post',
            name='rating_post',
            field=models.IntegerField(default=0, verbose_name='рейтинг'),
        ),
        migrations.AlterField(
            model_name='post',
            name='text_post',
            field=models.TextField(verbose_name='текст'),
        ),
    ]
