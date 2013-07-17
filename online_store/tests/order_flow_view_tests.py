from django.test import TestCase
from django.test.client import Client
from online_store.models import *
from django.core.urlresolvers import reverse
from django.template import RequestContext

class OrderFlowViewTests(TestCase):

  def test_empty_cart(self):
    "visiting the cart before adding items should display an empty cart"
    test_client = Client()
    response = test_client.get(reverse('cart'))

    self.assertEquals(len(response.context['cart']), 0)

  def test_adding_item_to_cart(self):

    "posting to the cart url should add the product id and quantity to the session"

    merchant = Merchant.objects.create(name='test merchant')
    product = Product.objects.create(name='test product', price=100.00)
    merchant.products.add(product)

    test_client = Client()
    test_client.post(reverse('cart'), {'product_id':str(product.id)})

    self.assertEquals(test_client.session['cart'][product.id], 1)