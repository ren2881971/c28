#coding:utf-8
# Create your views here.
from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from models import Topic, TopicReply
from forms import NewTopicForm, EditTopicForm, TopicReplyForm

def forum(request):
	post = {}
	post['topics'] = Topic.objects.all()
	return render(request, 'forum.html', post)

def topic(request, id):
	post = {}
	post['topic'] = Topic.objects.get(id = id)
	post['replys'] = TopicReply.objects.filter(topic_id = id)

	reply = TopicReply(topic = Topic.objects.get(id = id))
	if request.method == 'POST':
		form = TopicReplyForm(instance = reply, data = request.POST)
		if form.is_valid():
			result = form.save()
			return HttpResponseRedirect('/topic/id=%s'%id)
	else:
		form = TopicReplyForm()
		post['form'] = form
		return render_to_response('topic.html', post, 
			context_instance = RequestContext(request))

def topic_new(request):
	if request.method == 'POST':
		form = NewTopicForm(request.POST)
		if form.is_valid():
			result = form.save()
			return HttpResponseRedirect('/topic/action/success/')
	else:
		form = NewTopicForm()
		return render_to_response('topic_new.html', {'form':form}, 
			context_instance = RequestContext(request))

def topic_delete(request, id):
	topic = Topic.objects.get(id = id)
	topic.delete()
	return HttpResponseRedirect('/topic/action/success/')

def topic_edit(request, id):
	topic = Topic.objects.get(id = id)
	if request.method == 'POST':
		form = EditTopicForm(instance = topic, data = request.POST)
		if form.is_valid():
			result = form.save()
			return HttpResponseRedirect('/topic/action/success')
	else:
		form = EditTopicForm(instance = topic)
		return render_to_response('topic_edit.html', {'form':form}, 
			context_instance = RequestContext(request))

##TAG: just for test
def topic_action_success(request):
	html = '<html><body><a href="/forum/">OK!</a></body></html>'
	return HttpResponse(html)


