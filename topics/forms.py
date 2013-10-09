#coding:utf-8
from django.forms import ModelForm, Textarea, TextInput
from models import Topic, TopicReply

class TopicForm(ModelForm):
	class Meta:
		model = Topic
		fields = ('name', 'content')
		widgets = {
			'name' : TextInput(attrs = {'size' : 80}),
			'content' : Textarea(attrs = {'cols' : 80, 'rows' : 8}),
		}

class TopicReplyForm(ModelForm):
	class Meta:
		model = TopicReply
		fields = ('content',)
		widgets = {
			'content' : Textarea(attrs = {'cols' : 80, 'rows' : 8}),
		}

class NewTopicForm(TopicForm):
	{}

class EditTopicForm(TopicForm):
	{}

