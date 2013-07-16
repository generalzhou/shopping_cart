from models import *
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404, redirect
from django.template import RequestContext


def merchant_home(request, slug):
  merchant = Merchant.objects.get(slug=slug)
  product_list = merchant.products.all()
  return render_to_response('merchant_home.html',
                            {'merchant': merchant,
                            'product_list': product_list},
                            context_instance=RequestContext(request))
