#coding:utf-8
from django.http import HttpResponse,HttpResponseRedirect
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
   if request.method == 'POST':
       form = SigninForm(request.POST)
       if form.is_valid():
           value = form.cleaned_data
           return render_to_response('account/welcome.html')
   else:
       form = SigninForm()
   return render_to_response('account/signin.html',{'form':form},context_instance=RequestContext(request))



