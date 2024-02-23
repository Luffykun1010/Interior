from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class user(models.Model):
    first_name=models.CharField(max_length=55)
    last_name=models.CharField(max_length=55)
    username=models.CharField(max_length=55,primary_key=True)
    password=models.CharField(max_length=55)
    adhar=models.CharField(max_length=55)
    address=models.TextField()
    phone=models.IntegerField()
    def __str__(self) -> str:
        return self.first_name + " " + self.last_name

class company(models.Model):
    name=models.CharField(max_length=55)
    location=models.CharField(max_length=55)
    phone=models.CharField(max_length=55)
    gstin=models.CharField(max_length=55)
    def __str__(self) -> str:
        return self.name


class sub_works(models.Model):
    name =models.CharField(max_length=55)
    address=models.CharField(max_length=55)
    phone=models.CharField(max_length=55)
    category=models.CharField(max_length=55)
    def __str__(self) -> str:
        return self.name

class works(models.Model):
    username=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=55)
    file=models.FileField(upload_to="uploads/")
    description=models.TextField()
    status=models.CharField(max_length=50)
    def __str__(self):
        return self.username.username

class workers(models.Model):
    username=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=55)
    address=models.CharField(max_length=55)
    phone=models.CharField(max_length=55)
    category=models.CharField(max_length=55,choices=[('Architecture','Architecture'),('Designers','Designers'),('Electricians','Electricians'),('Furniture','Furniture'),('Plumbers','Plumbers')])
    def __str__(self) -> str:
        return self.name

class contract_details(models.Model):
    work=models.ForeignKey(works,on_delete=models.CASCADE,related_name='work')
    worker=models.ForeignKey(workers,on_delete=models.CASCADE,related_name='worker')
    payment = models.IntegerField(default=0)
    status=models.CharField(max_length=50,choices=[('Accept','Accept'),('Reject','Reject'),('Pending','Pending')],default='Pending')
