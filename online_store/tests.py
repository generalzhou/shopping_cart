from django.test import TestCase
from online_store.models import *

class UnitTests(TestCase):

  def test_merchant_product_association(self):
    "Merchant should have products"
    merchant = Merchant.objects.create(name='test merchant')
    product = Product.objects.create(name='test product', price=100.00)
    merchant.products.add(product)

    self.assertEquals(merchant.products.all()[0], product)

  def test_cart_product_association(self):
    "Cart should have products"
    cart = Cart.objects.create(user_id=1)
    product = Product.objects.create(name='test product', price=100.00)
    cart.products.add(product)

    self.assertEquals(cart.products.all()[0], product)
  
  def test_order_product_association(self):
    "Order should have products"
    order = Order.objects.create(user_id=1, address_id=1)
    product = Product.objects.create(name='test product', price=100.00)
    order.products.add(product)

    self.assertEquals(order.products.all()[0], product)

  def test_order_address_association(self):
    "Order has an address"
    order = Order(user_id=1)
    address = Address.objects.create(user_id=1)
    order.address = address
    order.save()

    self.assertEquals(order.address, address)

  def test_user_address_association(self):
    "User should have addresses"
    user = User.objects.create()
    address = Address(user_id=1)
    user.address_set.add(address)

    self.assertEquals(user.address_set.all()[0], address)

  def test_user_order_association(self):
    "User should have orders"
    user = User.objects.create()
    order = Order(address_id=1)
    user.order_set.add(order)

    self.assertEquals(user.order_set.all()[0], order)

  def test_user_cart_association(self):
    "User should have carts"
    user = User.objects.create()
    cart = Cart()
    user.cart_set.add(cart)

    self.assertEquals(user.cart_set.all()[0], cart)