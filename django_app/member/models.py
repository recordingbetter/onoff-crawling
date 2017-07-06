from django.contrib.auth.models import AbstractUser
from django.db import models

from .apis import api_owner_num


class MyUser(AbstractUser):
    img_profile = models.ImageField(upload_to='user', blank=True)
    nickname = models.CharField(max_length=50, null=True)
    slack = models.EmailField(null=True)
    phone = models.CharField(max_length=15, null=True)


class SmsSend(models.Model):
    msg_type = models.CharField(max_length=3, default='sms')
    msg_getter = models.CharField(max_length=20, blank=False)
    msg_sender = models.CharField(max_length=20, blank=False, default=api_owner_num)
    msg_text = models.TextField(blank=False)
