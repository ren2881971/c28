from django.conf.urls import patterns, include, url
from c28.settings import STATIC_URL
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('c28.views',
   url(r'^$','index',name='index'),
)
