from django.contrib import admin

# Register your models here.
from crawling.models import MyUser

admin.site.register(MyUser)
