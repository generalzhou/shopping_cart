from django.test import TestCase
from django.test.client import Client
from online_store.models import *

class ContactListViewTests(TestCase):

  def test(self):
    "Merchant home view should send merchant and merchant products to the template"
    merchant = Merchant.objects.create(name='test merchant')
    product = Product.objects.create(name='test product', price=100.00)
    merchant.products.add(product)

    test_client = Client()
    response = test_client.get('/' + merchant.slug)
    self.assertEquals(response.context['merchant'], merchant)
    self.assertEqual(response.context['product_list'][0], merchant.products.all()[0])


