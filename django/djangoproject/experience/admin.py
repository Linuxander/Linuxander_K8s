from django.contrib import admin
from django import forms
from .models import Employer, Task, Technology

class AdminEmployer(admin.ModelAdmin):
    model = Employer
    list_display = ('company', 'title', 'city', 'state', 'start', 'present', 'publish', 'public')

class AdminTask(admin.ModelAdmin):
    model = Task
    list_display = ('employers_uuid', 'blurb', 'publish', 'public')

class AdminTechnology(admin.ModelAdmin):
	model = Technology
	list_display = ('name', 'public')

admin.site.register(Employer, AdminEmployer)
admin.site.register(Task, AdminTask)
admin.site.register(Technology, AdminTechnology)