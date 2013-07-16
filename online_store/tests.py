# class Address(models.Model):
#   user = models.ForeignKey(User)
#   address_type = models.CharField(max_length=255,)
#   address = models.CharField(max_length=255,)
#   city = models.CharField(max_length=255,)
#   state = models.CharField(max_length=2,)
#   postal_code = models.CharField(max_length=20)

#   class Meta:
#     unique_together = ('user', 'address_type',)
# class Product(models.Model):
#   name = models.CharField(max_length=256) 
#   description = models.TextField()  
#   price = models.DecimalField(max_digits=4, decimal_places=2)
# class Merchant(models.Model):
#   name = models.CharField(max_length=256)
#   products = models.ManyToManyField(Product)  
# class Order(models.Model):
#   user = models.ForeignKey(User)
#   products = models.ManyToManyField(Product)
#   order_date = models.DateTimeField(auto_now_add=True)
#   address = models.ForeignKey(Address)
# class Cart(models.Model):
#   user = models.ForeignKey(User)
#   products = models.ManyToManyField(Product)

from django.test import TestCase
from online_store.models import *

class UnitTests(TestCase):

	def merchant_product_association(self):
		merchant = Merchant.objects.create(name='test merchant')
		product = Product.objects.create(name='test product', price=100.00)
		merchant.products.add(product)

		self.assertEquals(merchant.product.all()[0], product)

	def cart_product_association(self):
		cart = Cart.objects.create()
		product = Product.objects.create(name='test product', price=100.00)
		cart.products.add(product)

		self.assertEquals(cart.product.all()[0], product)
	
	def order_product_association(self):
		order = Order.objects.create()
		product = Product.objects.create(name='test product', price=100.00)
		cart.products.add(product)

		self.assertEquals(order.product.all()[0], product)

	def order_address_association(self):
		order = Order.objects.create()
		address = address.objects.create()
		order.address = address
		order.save()

		self.assertEquals(order.address, address)

	def user_address_association(self):
		user = User.objects.create()
		address = Address.objects.create()
		user.address_set.add(address)
		self.assertEquals(user.address_set.all()[0], address)

	def user_order_association(self):
		user = User.objects.create()
		order = Order.objects.create()
		user.order_set.add(order)
		self.assertEquals(user.order_set.all()[0], order)

	def user_cart_association(self):
		user = User.objects.create()
		cart = Cart.objects.create()
		user.order_set.add(cart)
		self.assertEquals(user.cart_set.all()[0], cart)




