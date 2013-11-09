#coding:utf-8
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from account.models import Account
from django.contrib.auth.models import User
from account.form import SigninForm,LoginForm
import logging
logger = logging.getLogger('django')
def signup(request):
    return render_to_response('account/regist.html',context_instance=RequestContext(request))
def regist(request):
   if request.method == 'POST':
       form = SigninForm(request.POST)
       if form.is_valid():
           value = form.cleaned_data
           user = User(email=value['email'],username = value['email'],password = value['password'])
           user.save()
           account = Account(user=user,nickname = value['nickname'])
           account.save()
           request.session['usr'] = account
           return render_to_response('account/welcome.html',{'nickname':value['nickname']},context_instance=RequestContext(request))
   else:
       form = SigninForm()
   return render_to_response('account/regist.html',{'form':form},context_instance=RequestContext(request))

def login(request):
    return render_to_response('account/login.html',context_instance = RequestContext(request))


def loginSubmit(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            value = form.cleaned_data
            user = User.objects.get(email = value['email'])
            logger.info("============="+user.email+"==================")
            if user.password == value['password']:
                account = Account.objects.get(user=user)
                logger.info("================已经验证成功")
                request.session['usr'] = account
                return render_to_response('account/welcome.html',{'nickname':account.nickname},context_instance=RequestContext(request))
    else:
        form = LoginForm()
        logger.info("======验证失败=======")
    return render_to_response('account/login.html',{'form':form},context_instance = RequestContext(request))

