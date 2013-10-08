from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth.views import login,logout
urlpatterns = patterns('account.views',
   url(r'^$','signup'),
   url(r'login/$',login),
   url(r'logout/$',logout),
   url(r'^regist/$','regist'),
)


urlpatterns += staticfiles_urlpatterns()