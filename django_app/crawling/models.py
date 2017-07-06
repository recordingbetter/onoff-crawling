
from django.db import models
from member.models import MyUser


class Keyword(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    text = models.CharField(max_length=50)
    created_date = models.DateTimeField(auto_now_add=True)


class News(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    detail_link = models.CharField(max_length=200)
    img_news = models.ImageField(upload_to='news', blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
