from pyexpat import model
from unittest.util import _MAX_LENGTH
from django.db import models

class Main(models.Model):
    img = models.ImageField(upload_to="Main/")
    title = models.CharField(max_length=50)
    text = models.CharField(max_length=255)

class Ad(models.Model):
    img = models.ImageField(upload_to="Ad/")
    title = models.CharField(max_length=40)
    text = models.CharField(max_length=300)
    category = models.CharField(max_length=15)
    comments = models.IntegerField()

class RecentGame(models.Model):
    img = models.ImageField(upload_to="RecentGame/")
    title = models.CharField(max_length=50)
    text = models.CharField(max_length=300)
    comments = models.IntegerField()
    category = models.CharField(max_length=15)

class GameInfo(models.Model):
    img = models.ImageField(upload_to="gameinfo/")
    name = models.CharField(max_length=50)
    musobaqa = models.CharField(max_length=50)
    end = models.CharField(max_length=50)
    teams = models.CharField(max_length=50)
    prize1 = models.IntegerField()
    prize2 = models.IntegerField()
    prize3 = models.IntegerField()

class Recent(models.Model):
    img = models.ImageField(upload_to="Recent/")
    name = models.CharField(max_length=50)
    text = models.CharField(max_length=255)
    score = models.CharField(max_length=255)

    
# Contact

class Map(models.Model):
    link = models.CharField(max_length=500)

class Email(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)
    message = models.CharField(max_length=200)
    def __str__(self):
        return self.email

class ContactUs(models.Model):
    text = models.CharField(max_length=255)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    email = models.EmailField()
    def __str__(self):
        return self.email
    


    
