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