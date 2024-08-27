from django.contrib import admin
from django import forms
from .models import Content

class AdminContent(admin.ModelAdmin):
    model = Content
    list_display = ('title', 'publish')

admin.site.register(Content, AdminContent)