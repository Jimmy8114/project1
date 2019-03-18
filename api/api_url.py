from django.conf.urls import *
from . import views, tests

app_name='api'
urlpatterns = [
    url(r'getlist/',views.getlist, name='getlist'),
    url(r'^human/(?P<pk>[0-9]+)/$', views.human_detail, name='human'),
    url(r'mixin/',views.HumanVS, name='mixin'),
    url(r'test/',views.test, name='test'),
    url(r'demo/',views.demotest, name='demo'),
    url(r'^modify/(?P<pk>[0-9]+)/$', views.modify, name='modify'),
    url(r'create/',views.create, name='create'),
]