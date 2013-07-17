from online_store.models import *
from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404, redirect
from django.template import RequestContext

def get_product_attributes_from_session(request):
  cart = []
  if 'cart' in request.session:
    for product_id, quantity in request.session['cart'].iteritems():
      product = Product.objects.get(id=product_id)
      cart.append({'id': product.id,
                    'name': product.name, 
                    'price': product.price,
                    'url': product.get_url(),
                    'quantity': quantity})

  return cart

def add_item_to_cart(request, quantity=1):
  product_id = int(request.POST['product_id'])
  if not request.session.get('cart', False):
    request.session['cart'] = {}
  
  cart = request.session['cart']

  if product_id in cart:
    cart[product_id] += quantity
  else:
    cart[product_id] = quantity

def cart(request):
  
  if request.method == 'POST':
    add_item_to_cart(request)
    request.session.modified = True

  cart = get_product_attributes_from_session(request)

  return render_to_response('cart.html',
                            {'cart': cart},
                            context_instance=RequestContext(request))

    

