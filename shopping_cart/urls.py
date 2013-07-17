from django.conf.urls import patterns, include, url
from online_store.views import *
from django.contrib import admin
from django.contrib import auth
admin.autodiscover()

urlpatterns = patterns('',

  url(r'^$', 
    'online_store.views.merchant_list',
    name='home'
  ),
  url(r'^accounts/login\/?$', 
    'django.contrib.auth.views.login',
    name='login'
  ),
  url(r'^accounts/logout\/?$', 
    'online_store.views.my_logout',
    name='logout'
  ),
  url(r'^accounts/signup\/?$',
    'online_store.views.signup',
    name='signup'
  ),
  url(r'^accounts/profile\/?$',
    'online_store.views.profile',
    name='profile'
  ),
  url(r'^accounts/cart\/?$',
    'online_store.views.cart',
    name='cart'
  ),
  url(r'^admin/doc/', 
    include('django.contrib.admindocs.urls')
  ),
  url(r'^admin/', 
    include(admin.site.urls)
  ),
  url(r'^(?P<merchant_slug>[-\w]+)\/?$', 
    'online_store.views.merchant_home', 
    name='merchant_home'
  ),
  url(r'^(?P<merchant_slug>[-\w]+)/product/(?P<product_slug>[-\w\d]+),(?P<id>\d+)\/?$', 
    'online_store.views.product_detail', 
    name='product_detail'
  )
)
