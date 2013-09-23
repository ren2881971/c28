#coding:utf-8
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from account.models import Account
from django.contrib.auth.models import User
def signup(request):
    return render_to_response('account/signin.html',context_instance=RequestContext(request))
def signin(request):
   if request.user.is_authenticated():
       return render_to_response('account/warning.html',{'message':u'你已经登录'},context_instance=RequestContext(request))

