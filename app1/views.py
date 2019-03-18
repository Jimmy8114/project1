from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
import json
import redis
from app1.models import BlogsPost
from . import form

# Create your views here.
def func1(request):
    print("I am func1")
    return render_to_response('page1.html')

def func2(request):
    print("I am func2")
    return render_to_response('page2.html')

def doFunc(request,pn):
    if (pn == '1'):
        return render_to_response('page1.html')
    elif (pn == '2'):
        return render_to_response('page2.html')
    else:
        return render_to_response('page3.html')

def getReq(r):   #request就是浏览器访问时地址后面带的参数，例如?k1=chen & k2=haoyu
    rst = "";
    for k,v in r.GET.items():
        rst += k + "-->" + v
        rst += ","
    return HttpResponse("Get value of Request is {0}".format(rst))

def render_test(request):
    #c是环境变量，传到模板里显示在浏览器中
    c = dict()
    c["name"] = "chenhaoyu"
    c["age"] = "18"
    c["sex"] = "male"

    #连接redis数据库
    r = redis.Redis(host='127.0.0.1',port=6379,db=0)
    r.set('myName','redisName')
    myName = r.get('myName').decode()  #bytes转string类型
    print(myName)
    c["myName"] = myName
    return render(request,"page3.html",context=c)

def getBlogList(request):
    bloglist = BlogsPost.objects.all()
    return  render_to_response('bloglist.html', { 'bloglist':bloglist })

from .models import Teacher
def teacherRegister(request):
    if request.method == 'GET':
        render(request,'teacherMsg.html')

    if request.method == 'POST':
        #往数据库里写数据方式一：
        '''teach = Teacher()
        teach.name = request.POST.get('name')
        teach.age = request.POST.get('age')
        teach.address = request.POST.get('address')
        teach.save()'''
        # 往数据库里写数据方式二：
        Teacher.objects.create(name = request.POST.get('name'),age = request.POST.get('age'),address = request.POST.get('address'))

    #显示添加后的数据表信息
    teacherList = Teacher.objects.all()
    return render_to_response('bloglist.html',{'teacherList':teacherList})
    #return HttpResponse('add teacher success')

def teacherMsg(r):
    return render(r,"teacherMsg.html")

#通过django的forms.ModelForm去接收前台html数据
def addTeacher(request):
   tFrom = form.AddTeacherFrom(request.POST)
   if tFrom.is_valid():
       tFrom.save()
       # 显示添加后的数据表信息
       teacherList = Teacher.objects.filter(name="chenhy")
       return render_to_response('bloglist.html', {'teacherList': teacherList})

#验证htlm页面输入框的数据
from django.views.generic import View
from .form import MyForm

class FromView(View):
    def get(self,request):
        return render(request,'teacherMsg.html')

    def post(self,request):
        form1 = MyForm(request.POST)
        if form1.is_valid():
            return HttpResponse('success')
        else:
            print(form1.errors.get_json_data())
            return HttpResponse('fail')

#********************* 通过Oauth2.0进行第三方平台验证 *********************
from django.http import HttpResponseRedirect
from django.conf import settings
from .oauth_client import OAuth_GITHUB,OAuth_QQ
from .models import OAuth_ex,User
from django.contrib.auth import login as auth_login, authenticate
#from django.core.urlresolvers import reverse
import time,uuid

def login(request):
    return render(request,'login.html')

def git_login(request):  #获取code
    oauth_git = OAuth_GITHUB(settings.GITHUB_APP_ID,settings.GITHUB_KEY,settings.GITHUB_CALLBACK_URL)
    url = oauth_git.get_auth_url()
    return HttpResponseRedirect(url)

def git_check(request):
    type = '1'
    request_code = request.GET.get('code')
    oauth_git = OAuth_GITHUB(settings.GITHUB_APP_ID, settings.GITHUB_KEY, settings.GITHUB_CALLBACK_URL)
    try:
        access_token = oauth_git.get_access_token(request_code)  # 获取access token
        time.sleep(0.1)  # 此处需要休息一下，避免发送urlopen的10060错误
    except:  # 获取令牌失败，反馈失败信息
        data = {}
        data['goto_url'] = '/'
        data['goto_time'] = 10000
        data['goto_page'] = True
        data['message_title'] = '登录失败'
        data['message'] = '获取授权失败，请确认是否允许授权，并重试。若问题无法解决，请联系网站管理人员'
        return render_to_response('response.html', data)

    infos = oauth_git.get_user_info()  # 获取用户信息
    nickname = infos.get('login', '')
    image_url = infos.get('avatar_url', '')
    open_id = str(oauth_git.openid)
    signature = infos.get('bio', '')
    if not signature:
        signature = "无个性签名"
    githubs = OAuth_ex.objects.filter( openid=open_id, type=type )  # 查询是否该第三方账户已绑定本网站账号
    if githubs.exists():  # 若已绑定，直接登录
        ct = dict()
        ct["username"] = githubs[0].user.userName
        return render(request,'main.html',context=ct)
        '''
        auth_user = authenticate(username = githubs[0].user.userName, password = githubs[0].user.password)
        if auth_user is not None:
            if auth_user.is_active:
               auth_login(request, auth_user, backend='django.contrib.auth.backends.ModelBackend')
               return HttpResponseRedirect('/')
        '''

    else:
        while User.objects.filter(userName=nickname):
            nickname = nickname + '*'
        user = User(userName = nickname, password = str(uuid.uuid1()), email = '496420626@qq.com')
        user.is_active = True
        user.save()

    oauth_ex = OAuth_ex(user = user,openid = open_id, type = type)
    oauth_ex.save()
    auth_login(request, user, backend='django.contrib.auth.backends.ModelBackend')
    data = {}  # 反馈登陆结果
    data['goto_url'] = '/'
    data['goto_time'] = 10000
    data['goto_page'] = True
    data['message_title'] = '绑定用户成功'
    data['message'] = u'绑定成功！您的用户名为：<b>%s</b>。您现在可以同时使用本站账号和此第三方账号登录本站了！' % nickname
    return render_to_response('response.html', data)


def qq_login(request):
    oauth_qq = OAuth_QQ(settings.QQ_APP_ID, settings.QQ_KEY, settings.QQ_CALLBACK_URL)
    url = oauth_qq.get_auth_url()
    return HttpResponseRedirect(url)


def qq_check(request):
    type = 2
    code = request.GET.get('code', '')
    oauth_qq = OAuth_QQ(settings.QQ_APP_ID, settings.QQ_KEY, settings.QQ_CALLBACK_URL)
    try:
        access_token = oauth_qq.get_access_token(code)
        time.sleep(0.1)
    except:
        data = {}
        data['goto_url'] = '/'
        data['goto_time'] = 10000
        data['goto_page'] = True
        data['message_title'] = '登录失败'
        data['message'] = '获取授权失败，请确认是否允许授权，并重试。若问题无法解决，请联系网站管理人员'
        return render_to_response('response.html', data)

    openid = oauth_qq.get_open_id()
    qqs = OAuth_ex.objects.filter(openid=openid, type=type)
    if qqs:
        auth_login(request, qqs[0].user, backend='django.contrib.auth.backends.ModelBackend')
        return HttpResponseRedirect('/')


#调用rest_framework API接口
from api.views import getlist

#def testAPI(request):










