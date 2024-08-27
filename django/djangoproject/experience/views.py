from django.shortcuts import render, HttpResponse
from experience.models import Employer, Task

def experience(request):
	employers = Employer.objects.filter(publish=True,public=True).order_by('-end', '-present')
	tasks = Task.objects.filter(publish=True,public=True)
	args = { 'employers' : employers, 'tasks' : tasks }
	return render(request, 'experience/experience.html', args)