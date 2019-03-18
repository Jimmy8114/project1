from django.db import models

# Create your models here.
class BlogsPost(models.Model):
    title = models.CharField(max_length = 150)
    body = models.TextField()
    timestamp = models.DateTimeField()

class Teacher(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    address = models.CharField(max_length=100)

    def __str__(self):   #魔法函数，可在shell窗口显示类属性
        return self.name

class School(models.Model):
    school_id = models.IntegerField()
    school_name = models.CharField(max_length=20)
    def __str__(self):   #魔法函数，可在shell窗口显示类属性
        return self.school_name

class Manager(models.Model):
    manager_id = models.IntegerField()
    manager_name = models.CharField(max_length=20)
    my_school = models.OneToOneField(School,on_delete=models.CASCADE,)   #Manager类和School类建立一对一关系
    def __str__(self):   #魔法函数，可在shell窗口显示类属性
        return self.manager_name

class Student(models.Model):
    student_id = models.IntegerField()
    student_name = models.CharField(max_length=20)
    my_school = models.ForeignKey("School",on_delete=models.CASCADE,)  #School类和Student类建立一对多关系
    def __str__(self):   #魔法函数，可在shell窗口显示类属性
        return self.student_name

class Professor(models.Model):
    professor_id = models.IntegerField()
    professor_name = models.CharField(max_length=20)
    students = models.ManyToManyField("Student")
    def __str__(self):   #魔法函数，可在shell窗口显示类属性
        return self.professor_name

#Oauth2.0第三方认证的模型

#本网站的用户模型
#用户登录的类型
type=(
    ('1','github'),
    ('2','qq')
)

class User(models.Model):
    userName = models.CharField(max_length=30)
    password = models.CharField(max_length=15,default='')
    email = models.CharField(max_length=30,default='')

class OAuth_ex(models.Model):
    user = models.ForeignKey("User",on_delete=models.CASCADE,)           #User为本网站的用户模型，每个第三方账号都要绑定本站账号
    openid = models.CharField(max_length=100,default='')
    type = models.CharField(max_length=1,choices=type)
