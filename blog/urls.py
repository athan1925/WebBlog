from django.urls import path, re_path
from django.conf.urls import  url
from . import views




urlpatterns = [
    path('', views.blog_list, name="blogs"),
#    url(r'^(?P<slug>[\w-]+)/$', views.blog_details, name="details"),
    ]