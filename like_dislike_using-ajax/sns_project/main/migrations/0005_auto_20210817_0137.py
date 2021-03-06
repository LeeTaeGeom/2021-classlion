# Generated by Django 3.2.5 on 2021-08-17 01:37

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0004_dislike_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='dislike_user_set',
            field=models.ManyToManyField(blank=True, related_name='dislikes_user_set', through='main.Dislike', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='post',
            name='like_user_set',
            field=models.ManyToManyField(blank=True, related_name='likes_user_set', through='main.Like', to=settings.AUTH_USER_MODEL),
        ),
    ]
