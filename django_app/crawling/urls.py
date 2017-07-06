from django.conf.urls import url
from . import views

app_name = 'news'
urlpatterns = [
    url(r'^$', views.news_list, name='news_list'),
    url(r'^news_search/$', views.news_search, name='news_search'),
]