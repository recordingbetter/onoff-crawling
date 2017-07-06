from django.conf.urls import url
from . import views

app_name = 'news'
urlpatterns = [
    url(r'^(?P<user_id>\d+)$', views.news_list, name='news_list')
]