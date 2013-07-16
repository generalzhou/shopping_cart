from django.db import models
from django.contrib.auth.models import User

class Address(models.Model):
  user = models.ForeignKey(User)

  address_type = models.CharField(max_length=255,)
  address = models.CharField(max_length=255,)
  city = models.CharField(max_length=255,)
  state = models.CharField(max_length=2,)
  postal_code = models.CharField(max_length=20)

  class Meta:
    unique_together = ('user', 'address_type',)

class Product(models.Model):
  name = models.CharField(max_length=256) 
  description = models.TextField()  
  price = models.DecimalField(max_digits=7, decimal_places=2)

class Merchant(models.Model):
  name = models.CharField(max_length=256)
  products = models.ManyToManyField(Product)  

class Order(models.Model):
  user = models.ForeignKey(User)
  products = models.ManyToManyField(Product)
  order_date = models.DateTimeField(auto_now_add=True)
  address = models.ForeignKey(Address)

class Cart(models.Model):
  user = models.ForeignKey(User)
  products = models.ManyToManyField(Product)
