#coding:utf-8
from django.db import models
from account.models import Account

# Create your models here.

#TODO: 
#class Forum(models.Model)
#	topic_count()

class Topic(models.Model):
    account = models.ForeignKey(Account, help_text = '发帖人id,如果未登录就为-1')
    #TAG： 未登录记为-1，这点貌似不可能
    name = models.CharField(max_length = 500, help_text = '帖子主题')
    content = models.TextField(help_text = '帖子内容')
    date = models.DateField(auto_now_add = True, help_text = '发帖日期')

    def __unicode__(self):
        return self.name  

class Topic_reply(models.Model):
    topic = models.ForeignKey(Topic, related_name = 'topic_reply', help_text = '回复的帖子id')
    account = models.ForeignKey(Account, help_text = '发帖人id,如果未登录就为-1')
    #TAG： 未登录记为-1，这点貌似不可能
    conten = models.TextField(help_text = '帖子内容')
    date = models.DateField(auto_now_add = True, help_text = '回复时间')

    def __unicode__(self):
        return u'%s: %d'%(self.topic.name, self.id)
