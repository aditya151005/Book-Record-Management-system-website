# create define models 
from django.db import models 
from django.contrib.auth.models import User
# Create your models here.
class Book(models.Model):
    title=models.CharField(max_length=100)
    price=models.FloatField()
    author=models.CharField(max_length=100)
    publisher=models.CharField(max_length=100)
class BRMuser(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    nickname=models.CharField(max_length=20,null=False)
