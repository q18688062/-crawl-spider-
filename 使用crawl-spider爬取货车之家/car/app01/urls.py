from django.conf.urls import url, include
from app01 import views

urlpatterns = [

    url(r'^index/$', views.index, name='index'),
    url(r'^detail/$', views.detail, name='detail'),
    url(r'^pic/(.*)', views.pic, name='pic'),

]