from models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from online_store.forms import *

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

def my_logout(request):
  logout(request)
  return redirect('login')

def signup(request,*args, **kwargs):

  if request.method == 'GET':
    return render_to_response('registration/signup.html',
                              {'form': SignupForm},
                              context_instance=RequestContext(request))

  elif request.method == 'POST':
    form = SignupForm(request.POST)
    if form.is_valid():
      username = form.cleaned_data['username']
      email = form.cleaned_data['email']
      password = form.cleaned_data['password']
      User.objects.create_user(username, email, password)
      user = authenticate(username=username, password=password)
      login(request, user)
      return render_to_response('registration/profile.html',
                                context_instance=RequestContext(request))

    else:
      return render_to_response('registration/signup.html',
                                {'form': SignupForm(request.POST)},
                                context_instance=RequestContext(request))

@login_required()
def account(request):
  return render_to_response('registration/profile.html',
                            {'user': request.user},
                            context_instance=RequestContext(request))

# @login_required()
# def checkout(request)