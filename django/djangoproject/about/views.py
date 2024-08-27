from django.shortcuts import render, HttpResponse
from about.models import Content

def about(request):
	content = Content.objects.all()
	args = { 'contents' : content }
	return render(request, 'about/about.html', args)