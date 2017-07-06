from django.contrib import admin
from .models import News

class PostAdmin(admin.ModelAdmin):
    # list_display = ['id', 'author', 'created_at', 'updated_at']
    pass
admin.site.register(News, PostAdmin)
