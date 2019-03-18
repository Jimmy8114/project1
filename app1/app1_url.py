from django.conf.urls import *
from . import views

app_name='app1'
urlpatterns = [
    url(r'(?:func(?P<pn>\d+)/)$',views.doFunc),  #正则表达式匹配路由func+整数
    url(r'getReq/',views.getReq),
    url(r'myMessage/',views.render_test),
    url(r'blog/',views.getBlogList),
    url(r'register/',views.teacherRegister),
    url(r'teacher/',views.teacherMsg),
    url(r'addTeacher/',views.addTeacher),
    url(r'git_check/',views.git_check, name='git_check'),
    url(r'git_login/',views.git_login, name='git_login'),
    url(r'qq_check/',views.qq_check, name='qq_check'),
    url(r'qq_login/',views.qq_login, name='qq_login'),
    url(r'login/',views.login, name='login'),
]