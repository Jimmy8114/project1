"""project1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app1 import app1_url,views
from app2 import app2_url,views
from api import api_url, views
from django.conf.urls import *
from rest_framework import routers

#router = routers.SimpleRouter()   #定义restful的路由
#router.register(r'human',views.HumanVS, base_name="human")   #注册路由
#router.register(r'getlist',views.getlist, base_name="getlist")

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'app1/',include(app1_url)),   #一级路由app1转发到二级路由app1_url.py，具体再由二级路由去处理
    url(r'app2/',include(app2_url)),
    url(r'api/',include(api_url)),
]
