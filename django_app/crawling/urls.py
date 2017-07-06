from django.conf.urls import url
from django import views

app_name = 'news'
urlpatterns = [
    url(r'^$', views.news_list, name='news_list')
]