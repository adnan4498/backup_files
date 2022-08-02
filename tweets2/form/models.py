from email.policy import default
from tkinter import CASCADE
from typing import List
from django import forms
from djongo import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

class Mentions(models.Model):
    screen_name = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    id = models.CharField(max_length=30)

    class Meta:
        abstract = True

class Urls(models.Model):
    urls = models.CharField(max_length=50)

    class Meta:
        abstract = True
        
    def _str_(self):
        return self.urls

class Photos(models.Model):
    photos = models.CharField(max_length=50)
   
    class Meta:
        abstract = True
        
    def _str_(self):
        return self.photos

class Hashtags(models.Model):
    hashtags = models.CharField(max_length=50)

    class Meta:
        abstract = True
        
    def _str_(self):
        return self.hashtags

class Label(models.Model):
    label = models.CharField(max_length=50)
   
    class Meta:
        abstract = True
        
    def _str_(self):
        return self.label

class Labels(models.Model):
    _id = models.ObjectIdField()
    label = models.ArrayField(model_container=Label)
  
    def _str_(self):
        return str(self.label)

class Posts(models.Model):
    _id = models.ObjectIdField()
    created_at = models.DateTimeField()
    date = models.DateField()
    time = models.TimeField()
    timezone = models.CharField(max_length=20)
    user_id = models.CharField(max_length=40)
    username = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    language = models.CharField(max_length=10)
    mentions = models.ArrayField(model_container=Mentions)
    urls = models.ArrayField(model_container=Urls)
    photos = models.ArrayField(model_container=Photos)
    replies_count = models.IntegerField()
    retweet_count = models.IntegerField()
    likes_count = models.IntegerField()
    hashtags = models.ArrayField(model_container=Hashtags)
    content_Link = models.CharField(max_length=50)
    content = models.CharField(max_length=200)
    label = models.ArrayField(model_container=Label)
    

    def _str_(self):
        return str(self.username)