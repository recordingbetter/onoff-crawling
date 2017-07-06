from django.contrib.auth.models import AbstractUser
from django.db import models


class MyUser(AbstractUser):
    img_profile = models.ImageField(upload_to='user', blank=True)
    slack = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=15, blank=True)
    nickname = models.CharField(max_length=20)


class News(models.Model):
    user = models.ForeignKey(MyUser)
    title = models.CharField(max_length=100)
    detail_link = models.CharField(max_length=200)
    img_news = models.ImageField(upload_to='news', blank=True)
    created_date = models.DateTimeField(auto_now_add=True)


class Keyword(models.Model):
    user = models.ForeignKey(MyUser)
    text = models.CharField(max_length=50)
    created_date = models.DateTimeField(auto_now_add=True)


