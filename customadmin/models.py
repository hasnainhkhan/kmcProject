from django.db import models

# Create your models here.
class Nmgmt(models.Model): #notice management table
    sno=models.AutoField(primary_key=True)
    msg=models.TextField(max_length=500)
    timeStamp=models.DateTimeField(auto_now_add=True,blank=True)