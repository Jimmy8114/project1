from django.db import models

# Create your models here.
class Computer(models.Model):
    computerName = models.CharField(max_length=20)
    price = models.IntegerField()
    discription = models.CharField(max_length=100)

class Iphone(models.Model):
    iphoneName = models.CharField(max_length=20)
    price = models.IntegerField()
    discription = models.CharField(max_length=100)

class Account(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)