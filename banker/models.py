from django.db import models
from datetime import date
from django.utils import timezone

# Create your models here.

class userinfo(models.Model):
    user_img = models.ImageField(upload_to='images/', default='images/profile.jpg')
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    mobile_no = models.IntegerField()
    current_balance = models.IntegerField()
    dob = models.DateTimeField(default=None)
    age = models.IntegerField(default=18)

    def __str__(self):
        return self.name

class TransferInfo(models.Model):
    sender_name = models.CharField(max_length=100)
    reciever_name = models.CharField(max_length=100)
    amount = models.IntegerField()
    date = models.DateField()
    time = models.TimeField()
