#coding:utf-8
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from account.models import Account
from django.contrib.auth.models import User
from account.form import SigninForm
import logging
logger = logging.getLogger('django')
def signup(request):
    return render_to_response('account/signin.html',context_instance=RequestContext(request))
def signin(request):


   return HttpResponse('<b>Welcome</b?')