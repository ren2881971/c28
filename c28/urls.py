#coding:utf-8
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
   url(r'forum/$', 'forum'),
   url(r'topic/id=(?P<id>\d+)/$', 'topic'),
   url(r'topic/new/$', 'topic_new'),
   url(r'topic/action/success/$', 'topic_action_success'),
   url(r'topic/delete/id=(?P<id>\d+)/$', 'topic_delete'),
   url(r'topic/edit/id=(?P<id>\d+)/$', 'topic_edit'),
#   url(r'topic/reply/id=(?P<id>\d+)/$', 'topic_reply'),
)

##TAG: admin MODE
urlpatterns += patterns('',
   url(r'^admin/', include(admin.site.urls)),
)