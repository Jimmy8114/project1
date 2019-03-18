from django.db import models

# Create your models here.
class Human(models.Model):
    humanName = models.CharField(max_length=20)
    humanAge = models.IntegerField()