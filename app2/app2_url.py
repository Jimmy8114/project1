from django.conf.urls import *
from . import views

app_name='app2'
urlpatterns = [
    url(r'index/',views.index, name='index'),
    url(r'computer/',views.computer, name='computer'),
    url(r'iphone/',views.iphone, name='iphone'),
    url(r'login/',views.login, name='login'),
    url(r'tobase/',views.tobase, name='tobase'),
    url(r'company/',views.company, name='company'),
    url(r'profit/',views.profit, name='profit'),
]