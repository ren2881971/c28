#coding:utf-8
from django.db import models
from django.contrib.auth.models import User
class Account(models.Model):
    user = models.OneToOneField(User,related_name='user_profile',verbose_name=u'用户')
    nickname = models.CharField(max_length=50)
    photo = models.CharField(max_length=500)
    birthday = models.DateTimeField(blank=True)
    def __unicode__(self):
        return self.email
    class Meta:
        db_table = 'account'
