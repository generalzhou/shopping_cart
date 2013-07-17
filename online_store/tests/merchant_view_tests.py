from django.test import TestCase
from django.test.client import Client
from online_store.models import *

class MerchantListViewTests(TestCase):

  def test_merchant_home(self):
    "merchant_home view should send merchant and merchant products to the template"
    merchant = Merchant.objects.create(name='test merchant')
    product = Product.objects.create(name='test product', price=100.00)
    merchant.products.add(product)

    test_client = Client()
    response = test_client.get('/{0}'.format(merchant.slug))
    self.assertEquals(response.context['merchant'], merchant)
    self.assertEquals(response.context['product_list'][0], merchant.products.all()[0])

  def test_merchant_home_404(self):
    "mechant_home view should send 404 if slug doesn't match merchant"

    merchant = Merchant.objects.create(name='test merchant')

    test_client = Client()
    response = test_client.get('/{0}'.format('wrong-merchant-slug'))
    self.assertEquals(response.status_code, 404)  

  def test_product_detail(self):
    "product_detail view should send the merchant and product to the template"

    merchant = Merchant.objects.create(name='test merchant')
    product = Product.objects.create(name='test product', price=100.00)
    merchant.products.add(product)

    test_client = Client()
    response = test_client.get('/{0}/product/{1},{2}'.format(merchant.slug, product.slug, product.id))
    self.assertEquals(response.context['merchant'], merchant)
    self.assertEquals(response.context['product'], product)

  def test_product_detail_404(self):
    "product_detail view should send 404 if product does not belong to merchant"

    merchant = Merchant.objects.create(name='test merchant')
    product = Product.objects.create(name='test product', price=100.00)

    test_client = Client()
    response = test_client.get('/{0}/product/{1},{2}'.format(merchant.slug, product.slug, product.id))
    self.assertEquals(response.status_code, 404)