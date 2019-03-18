from django.conf.urls import *
from . import views

app_name='app2'
urlpatterns = [
    url(r'index/',views.index, name='index'),
    url(r'computer/',views.computer, name='computer'),
    url(r'iphone/',views.iphone, name='iphone'),
    url(r'login/',views.login, name='login'),
]