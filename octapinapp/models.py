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