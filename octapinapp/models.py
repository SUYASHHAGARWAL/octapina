from django.db import models

# Create your models here.
class Contact(models.Model):
    username = models.CharField(max_length=120,blank=False)
    email = models.CharField(max_length=50,blank=False,default='')
    mobile = models.CharField(max_length=14,blank=False,default='')
    message = models.CharField(max_length=300,blank=False)

class NewUserData(models.Model):
    username = models.CharField(max_length=120,blank=False,default='')
    useremail = models.CharField(max_length=120,blank=False,default='')
    usermobile = models.CharField(max_length=120,blank=False,default='')
    usercity = models.CharField(max_length=120,blank=False,default='')
    userdob = models.CharField(max_length=120,blank=False,default='')
    usergender = models.CharField(max_length=120,blank=False,default='')
    guardiansname = models.CharField(max_length=120,blank=False,default='')
    guardiansphone = models.CharField(max_length=120,blank=False,default='')
    userschool = models.CharField(max_length=120,blank=False,default='')
    userclass = models.CharField(max_length=120,blank=False,default='')
    userpassword = models.CharField(max_length=30,blank=False,default='')
    userbatch = models.CharField(max_length=200,blank=False,default='')
    batch_purchased = models.CharField(max_length=10,blank=False,default='')

class BatchInfo(models.Model):
    BatchName = models.CharField(max_length=100,blank=False,default='')
    Batchfees = models.CharField(max_length=12,blank=False,default='')
    BatchDfees = models.CharField(max_length=12,blank=False,default='')
    duration = models.CharField(max_length=12,blank=False,default='')
    startdate = models.CharField(max_length=15,blank=False,default='')

class admin(models.Model):
    mobilenum = models.CharField(max_length=12,blank=False,default='')
    adminname = models.CharField(max_length=50,blank=False,default='')
    password = models.CharField(max_length=42,blank=False,default='')

class Events(models.Model):
    eventdate = models.CharField(max_length=20,blank=False,default='')
    eventname = models.CharField(max_length=80,blank=False,default='')
    eventtime = models.CharField(max_length=20,blank=False,default='')
    organiser = models.CharField(max_length=20,blank=False,default='')
    eventlevel = models.CharField(max_length=30,blank=False,default='')