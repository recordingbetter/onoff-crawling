from django.conf.urls import url

from member import views

app_name = 'member'
urlpatterns = [
    url(r'^signup/$', views.signup, name='signup'),
    #url(r'^login/$', views.login, name='login'),
    #url(r'^my_profile/$', views.my_profile, name='my_profile'),
]