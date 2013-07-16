from django.conf.urls import patterns, include, url
from online_store.views import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^(?P<merchant_slug>[-\w]+)$', 
        'online_store.views.merchant_home', 
        name='merchant_home',
    ),
    url(r'^(?P<merchant_slug>[-\w]+)/product/(?P<product_slug>[-\w\d]+),(?P<id>\d+)$', 
        'online_store.views.product_detail', 
        name='product_detail',
    ),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
