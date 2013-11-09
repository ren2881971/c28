#coding:utf-8
from django import forms
from account.models import *
import datetime
class SigninForm(forms.Form):
    error_message = {
        'duplicate_email':u'您输入的邮箱已被注册',
        'password_error':u'密码输入不一致',
        'duplicate_nickname':u'昵称已经被注册',
    }
    nickname = forms.CharField(max_length=50,label=u'昵称',error_messages={'required':u'请输入昵称'})
    email = forms.EmailField(max_length=128,label=u'登陆邮箱',widget=forms.TextInput,error_messages=
    {'required':u'请输入注册邮箱','invalid':u'请输入有效的邮箱'}
    )
    password = forms.CharField(widget=forms.PasswordInput(render_value=False),label=u'输入密码',error_messages=
    {
        'required':u'请输入密码'
    }
    )
    password_confirm  = forms.CharField(label=u'请输入密码',widget=forms.PasswordInput(render_value=False),error_messages=
    {
        'required':u'请输入密码'
    })

    def clean(self):
        if "password" in self.cleaned_data and "password_confirm" in self.cleaned_data:
            if self.cleaned_data['password'] != self.cleaned_data['password_confirm']:
                raise forms.ValidationError(self.error_message['password_error'])
        return self.cleaned_data
    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            User.objects.get(email=email)
        except User.DoesNotExist:
            return email
        raise forms.ValidationError(self.error_message['duplicate_email'])
    def clean_nickname(self):
        nickname = self.cleaned_data['nickname']
        try:
            Account.objects.get(nickname = nickname)
        except Account.DoesNotExist:
            return nickname
        raise forms.ValidationError(self.error_message['duplicate_nickname'])
class LoginForm(forms.Form):
    error_message = {
        'userNotExist':u'用户不存在',
        'EmailOrPassWdWrong':u'用户名或密码错误',
    }
    email = forms.EmailField(max_length=128,label=u'登陆邮箱',widget=forms.TextInput,error_messages={
        'required':u'请输入登录邮箱','invalid':u'请输入有效的邮箱'
    })
    password = forms.CharField(widget=forms.PasswordInput(render_value=False),label=u'输入密码',error_messages=
    {
        'required':u'请输入密码'
    })
    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            User.objects.get(email = email)
        except User.DoesNotExist:
            raise forms.ValidationError(self.error_message['userNotExist'])
        return email
    '''
    def clean(self):
        password = self.cleaned_data['password']
        email = self.cleaned_data['email']
        user = User.objects.get(email = email)
        if user.password != password:
            raise forms.ValidationError(self.error_message['EmailOrPassWdWrong'])
        return self.cleaned_data
        '''


