from django.contrib.auth.models import AbstractUser
from django.db import models


class MyUser(AbstractUser):
    img_profile = models.ImageField(upload_to='user', blank=True)
    nickname = models.CharField(max_length=50)
    slack = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
