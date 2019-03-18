from . import models
from django import forms
import django

class AddTeacherFrom(forms.ModelForm):
    class Meta:
        model = models.Teacher
        fields = '__all__'  #指定模型中需要验证的字段，__all__代表所有字段

class MyForm(forms.Form):
    name = django.db.models.CharField(max_length=20)
    age = django.db.models.IntegerField()
    address = django.db.models.CharField(max_length=100)