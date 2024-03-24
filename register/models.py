from django.db import models

# Create your models here.
# apply hostel table
class Form(models.Model):
    sno=models.AutoField(primary_key=True)
    name=models.CharField(max_length=255)
    fname=models.CharField(max_length=255)
    contact=models.CharField(max_length=13)
    email=models.CharField(max_length=100)
    dob=models.CharField(max_length=20)
    address=models.TextField(max_length=255)
    idno=models.CharField(max_length=15)
    idimg=models.ImageField(upload_to="media/image/",max_length=250,null=True)
    rnumber=models.CharField(max_length=15)
    timeStamp=models.DateTimeField(auto_now_add=True,blank=True)
    def __str__(self):
        return 'request from: ' + self.name

# student profile  table
class StudentP(models.Model):
    pass
    