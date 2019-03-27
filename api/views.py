from django.shortcuts import render,HttpResponse
from rest_framework import viewsets,status,mixins,generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import HumanSerializer
from .models import Human
import json

# Create your views here.
class HumanVS(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Human.objects.all()
    serializer_class = HumanSerializer  #允许用户查看或编辑API端点

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    #def getdetail(self, request, *args, **kwargs):
     #   return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

'''
   查询所有记录以及新增一条记录的API接口，在前端html通过url访问API接口，接口返回数据
   给前端html
'''
@api_view(['GET','POST'])
def getlist(request,format=None):
    if request.method == "GET":     #查询所有记录
       humans = Human.objects.all()
       humanSer = HumanSerializer(humans,many=True)
       return Response(humanSer.data)
    elif request.method == "POST":   #新增一条记录
        serializer = HumanSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','POST','DELETE'])
def human_detail(request,pk,format=None):
    try:
        human = Human.objects.get(pk=pk)
    except Human.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        humanSer = HumanSerializer(human)
        return Response(humanSer.data)
    elif request.method == "POST":
        humanSer = HumanSerializer(human, data=request.data)
        if humanSer.is_valid():
            humanSer.save()
            return Response(humanSer.data)
        return Response(humanSer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        human.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

def test(request):
    return render(request,'getlist.html')

def demotest(request):
    return render(request,'demoTest.html')

def create(request):
    return render(request,'create.html')

def modify(request,pk):
    return render(request,'modify.html',{'pk': json.dumps(pk)})

#微信公众号开发
import hashlib
from django.utils.encoding import smart_str
from django.views.decorators.csrf import csrf_exempt

#这里使用@csrf_exempt去掉csrf防护
@csrf_exempt
def weixin_main(request):
    if request.method == "GET":
        # 接收微信服务器get请求发过来的参数
        signature = request.GET.get('signature', None)
        timestamp = request.GET.get('timestamp', None)
        nonce = request.GET.get('nonce', None)
        echostr = request.GET.get('echostr', None)
        # 服务器配置中的token
        token = 'chy'
        # 把参数放到list中排序后合成一个字符串，再用sha1加密得到新的字符串与微信发来的signature对比，如果相同就返回echostr给服务器，校验通过
        hashlist = [token, timestamp, nonce]
        hashlist.sort()
        hashstr = ''.join([s for s in hashlist])
        hashstr = hashlib.sha1(hashstr).hexdigest()
        if hashstr == signature:
            return HttpResponse(echostr)
        else:
            return HttpResponse("field")
    else:
        othercontent = autoReply(request)
        return HttpResponse(othercontent)

#微信服务器推送消息是xml的，根据利用ElementTree来解析出的不同xml内容返回不同的回复信息，就实现了基本的自动回复功能了，也可以按照需求用其他的XML解析方法
import xml.etree.ElementTree as ET
def autoReply(request):
    try:
        webData = request.body
        xmlData = ET.fromstring(webData)

        msg_type = xmlData.find('MsgType').text
        ToUserName = xmlData.find('ToUserName').text
        FromUserName = xmlData.find('FromUserName').text
        CreateTime = xmlData.find('CreateTime').text
        MsgType = xmlData.find('MsgType').text
        MsgId = xmlData.find('MsgId').text

        toUser = FromUserName
        fromUser = ToUserName

        if msg_type == 'text':
            content = "您好,欢迎来到Python大学习!希望我们可以一起进步!"
            replyMsg = TextMsg(toUser, fromUser, content)
            print
            "成功了!!!!!!!!!!!!!!!!!!!"
            print
            replyMsg
            return replyMsg.send()

        elif msg_type == 'image':
            content = "图片已收到,谢谢"
            replyMsg = TextMsg(toUser, fromUser, content)
            return replyMsg.send()
        elif msg_type == 'voice':
            content = "语音已收到,谢谢"
            replyMsg = TextMsg(toUser, fromUser, content)
            return replyMsg.send()
        elif msg_type == 'video':
            content = "视频已收到,谢谢"
            replyMsg = TextMsg(toUser, fromUser, content)
            return replyMsg.send()
        elif msg_type == 'shortvideo':
            content = "小视频已收到,谢谢"
            replyMsg = TextMsg(toUser, fromUser, content)
            return replyMsg.send()
        elif msg_type == 'location':
            content = "位置已收到,谢谢"
            replyMsg = TextMsg(toUser, fromUser, content)
            return replyMsg.send()
        else:
            msg_type == 'link'
            content = "链接已收到,谢谢"
            replyMsg = TextMsg(toUser, fromUser, content)
            return replyMsg.send()
    except Exception as e:
        return e.args

class Msg(object):
        def __init__(self, xmlData):
            self.ToUserName = xmlData.find('ToUserName').text
            self.FromUserName = xmlData.find('FromUserName').text
            self.CreateTime = xmlData.find('CreateTime').text
            self.MsgType = xmlData.find('MsgType').text
            self.MsgId = xmlData.find('MsgId').text

import time
class TextMsg(Msg):
        def __init__(self, toUserName, fromUserName, content):
            self.__dict = dict()
            self.__dict['ToUserName'] = toUserName
            self.__dict['FromUserName'] = fromUserName
            self.__dict['CreateTime'] = int(time.time())
            self.__dict['Content'] = content

        def send(self):
            XmlForm = """
            <xml>
            <ToUserName><![CDATA[{ToUserName}]]></ToUserName>
            <FromUserName><![CDATA[{FromUserName}]]></FromUserName>
            <CreateTime>{CreateTime}</CreateTime>
            <MsgType><![CDATA[text]]></MsgType>
            <Content><![CDATA[{Content}]]></Content>
            </xml>
            """
            return XmlForm.format(**self.__dict)

