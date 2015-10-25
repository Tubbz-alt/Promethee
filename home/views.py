from django.shortcuts import render
from django.template import RequestContext, loader
from django.http import HttpResponse

from .models import Project

# Create your views here.
def index(request):
    template = loader.get_template('home/index.html')
    context = RequestContext(request)
    return HttpResponse( template.render(context) )

def projects(request):	
	template = loader.get_template('home/projects.html')
	context = RequestContext(request, {"projects" : Project.objects.all()})
	return HttpResponse( template.render(context) )

def contact(request):
	template = loader.get_template('home/contact.html')
	context = RequestContext(request, {})
	return HttpResponse( template.render(context) )

def organization(request):
	template = loader.get_template('home/organization.html')
	context = RequestContext(request, {})
	return HttpResponse( template.render(context) )
