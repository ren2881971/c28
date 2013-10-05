#coding:utf-8
from django import forms
from models import Topic, Topic_reply

class TopicForm(forms.ModelForm):
	name = forms.CharField(label = u'主题', widget = forms.TextInput(attrs={'size':'80'}))
	content = forms.CharField(label = u'内容', widget = forms.Textarea(attrs={'cols':'95','rows':'14'}))

	class Meta:
		model = Topic

class NewTopicForm(TopicForm):
	def save(self):
#		if not self.name:
			##TODO:
		#else:
		post = Topic(name = self.cleaned_data['name'], content = self.cleaned_data['content'])
		post.save()
		return post

class EditTopicForm(TopicForm):
	def __init__(self, *args, **kwargs):
		super(EditTopicForm, self).__init__(*args, **kwargs)
		self.initial['name'] = self.instance.name
		self.initial['content'] = self.instance.content

	def save(self):
		post = self.instance
		post.name = self.cleaned_data['name']
		post.content = self.cleaned_data['content']
		post.save()
		return post