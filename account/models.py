#coding:utf-8
from django.db import models
from django.contrib.auth.models import User

class Account(models.Model):
    user = models.OneToOneField(User,related_name='user_profile',verbose_name=u'用户')
    nickname = models.CharField(max_length=50)
    photo = models.CharField(max_length=500)
    birthday = models.DateTimeField(blank=True)

## TAG：你暂时没有email啊，我先改成nickname了，不然调不过去 --by CC
    def __unicode__(self):
        return self.nickname
#    def __unicode__(self):
#        return self.nickname
    class Meta:
        db_table = 'account'
