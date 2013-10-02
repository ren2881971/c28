# Create your views here.
from django.shortcuts import render_to_response,get_object_or_404
from models import Topic, Topic_reply

def forum(request):
	return render_to_response('forum.html')

def topic(request):
	return render_to_response('topic.html')

def topic_new(request):
	return render_to_response('topic_new.html')