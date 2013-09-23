#coding:utf-8
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from account.models import Account
def signup(request):
    return render_to_response('account/signin.html',context_instance=RequestContext(request))
def signin(request):
    return HttpResponse("<b1>11</b1>")