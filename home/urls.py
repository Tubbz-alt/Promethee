from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^projects$', views.projects, name='projects'),
    url(r'^organization$', views.organization, name='organization'),
    url(r'^contact$', views.contact, name='contact'),
]
