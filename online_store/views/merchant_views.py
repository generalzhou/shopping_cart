from online_store.models import *
from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404, redirect
from django.template import RequestContext

def merchant_list(request):
	merchants = Merchant.objects.all()
	return render_to_response('merchant_list.html',
                            {'merchants': merchants},
                            context_instance=RequestContext(request))


def merchant_home(request, merchant_slug):
  merchant = get_object_or_404(Merchant, slug=merchant_slug)
  product_list = merchant.products.all()
  return render_to_response('merchant_home.html',
                            {'merchant': merchant,
                            'product_list': product_list},
                            context_instance=RequestContext(request))


def product_detail(request, merchant_slug, product_slug, id):
  merchant = get_object_or_404(Merchant, slug=merchant_slug)
  product = get_object_or_404(merchant.products, id=id)
  return render_to_response('product_detail.html',
                            {'merchant': merchant,
                            'product': product},
                            context_instance=RequestContext(request))
