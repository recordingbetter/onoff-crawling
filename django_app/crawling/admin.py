from django.contrib import admin
from .models import News

class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    pass
admin.site.register(News, PostAdmin)
