from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField('Name',max_length=100)
    price=models.DecimalField('Price',decimal_places=2,max_digits=18)
    stock=models.IntegerField('Quantity of Stock')
    def __str__(self):
        return f'{self.name} -- {self.price} $'
class Customer(models.Model):
    name= models.CharField('name', max_length=100)
    lastname=models.CharField('lastname',max_length=100)
    email=models.EmailField('Email',max_length=100)
    
    def __str__(self):
        return f'{self.name} -- {self.email}'