from django.db import models
# Create your models here.
class Companyreg(models.Model):
    userid=models.CharField(max_length=20)
    password=models.CharField(max_length=20)

class Add_Company(models.Model):
        name=models.CharField(max_length=30)
        symbol=models.CharField(max_length=1)
        password=models.CharField(max_length=10)
        email=models.EmailField(max_length=30)
        address=models.CharField(max_length=30)
        phonenumber=models.IntegerField()
        select=models.CharField(max_length=10)
        image=models.ImageField(upload_to='product_image/')

class Add_Agent(models.Model):
    id=models.AutoField(primary_key=True, max_length=1000)
    name=models.CharField(max_length=30)
    password=models.CharField(max_length=30)
    email=models.EmailField(max_length=30)
    address=models.CharField(max_length=30)
    phonenumber=models.IntegerField()
    image=models.ImageField(upload_to='product_image/')

class Customer_Registration(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=30)
    password=models.CharField(max_length=30)
    confirm=models.CharField(max_length=30)
    email=models.EmailField(max_length=30)
    address=models.CharField(max_length=30)
    phonenumber=models.CharField(max_length=30)
    image=models.ImageField(upload_to='product_image/')

class Shares_Add(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=30)
    symbol=models.CharField(max_length=1)
    price=models.IntegerField()
    quantity=models.IntegerField(default=0)
    select=models.CharField(max_length=30)


class Feedback(models.Model):
    email=models.EmailField(primary_key=True,max_length=50)
    name=models.CharField(max_length=50)
    feedback=models.CharField(max_length=100, default=0)

class Suggesstion(models.Model):
    email=models.EmailField(primary_key=True,max_length=30)
    name=models.CharField(max_length=50)
    suggession=models.CharField(max_length=100)


