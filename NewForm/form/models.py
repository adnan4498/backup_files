from django.db import models

# Create your models here.

class form(models.Model):
    product_id = models.AutoField
    db_FirstName = models.CharField(max_length=50,default="",null=True)
    db_LastName = models.CharField(max_length=50,default="",null=True)
    db_Cnic = models.CharField(max_length=50,default="",null=True)
    db_DOB = models.CharField(max_length=50,default=0,null=True)
    db_Adress = models.CharField(max_length=300,null=True)
  
  
   




