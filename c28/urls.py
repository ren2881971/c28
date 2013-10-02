#from django.conf.urls import patterns, include, url
from django.conf.urls.defaults import *
from c28.settings import STATIC_URL
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('c28.views',
   url(r'^$','index', name='index'),
   url(r'account/', include('account.urls')),
)

#urlpatterns += staticfiles_urlpatterns()

urlpatterns += patterns('topics.views',
   url(r'forum/', 'forum'),
   url(r'topic/new/', 'topic_new'),
#   url(r'topic/id=', )
)

##TAG: admin MODE
urlpatterns += patterns('',
   url(r'^admin/', include(admin.site.urls)),
)