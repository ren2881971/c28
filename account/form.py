#coding:utf-8
from django import forms
from account.models import *
class SigninForm(forms.Form):
    error_message = {
        'duplicate_email':u'您输入的邮箱已被注册',
        'password_error':u'密码输入不一致',
    }
    nickname = forms.CharField(max_length=50,label=u'昵称',error_messages={'required':u'请输入昵称'})
    email = forms.EmailField(max_length=128,label=u'登陆邮箱',widget=forms.TextInput,error_messages=
    {'required':u'请输入注册邮箱','invalid':u'请输入有效的邮箱'}
    )
    password = forms.CharField(widget=forms.PasswordInput(render_value=False),label=u'输入邮箱',error_messages=
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