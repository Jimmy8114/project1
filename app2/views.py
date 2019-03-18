from django.shortcuts import render,redirect
from app2.models import *
import json
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
# Create your views here.
def index(request):
   name = request.session.get("name")
   if name:
       msg = name + "，欢迎您光临我的主页面！"
       return render(request,"index.html",{'msg':msg})
   else:
       return redirect('/app2/login')


def computer(request):
    computers = Computer.objects.all()
    paginator = Paginator(computers,4)  #生成paginator对象，定义每页显示4条记录
    page = request.GET.get('page', 1)   #从页面获取当前页码数，默认为1
    currentpage = int(page)
    number=int((currentpage-1)*4)  #条数据编号

    try:
        computers = paginator.page(page)  #获取当前页的电脑记录,computers此时为page对象
    except PageNotAnInteger:
        computers = paginator.page(1)   #输入页码不是整数时，显示第1页的内容
    except EmptyPage:
        computers = paginator.page(paginator.num_pages) # 如果用户输入的页数不在系统的页码列表中时,显示最后一页的内容

    return render(request,"computer.html",{ 'computers':computers,'paginator':paginator,'currentpage':currentpage,'number':number })

def iphone(request):
    iphones = Iphone.objects.all()
    return render(request,"iphone.html",{ 'iphones':iphones })

def login(request):
    if request.method == "GET":
        return render(request,"login2.html")   #先打开登录输用户密码的界面
    else:
        name = request.POST.get("username")  #通过POST接收表单输入的用户密码
        pwd = request.POST.get("password")
        obj = Account.objects.filter(username=name, password=pwd).first()
        if obj:
            request.session["name"] = name
            return redirect("/app2/index")    #根据url，重定向到index(request)函数
        else:
            msg = "用户名/密码错误，请重新输入！"
            return render(request, 'login2.html', {'msg': json.dumps(msg)})   #这个msg是传递给js的，需要经过json.dumps处理
