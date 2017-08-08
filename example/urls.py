from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView


class SimpleStaticView(TemplateView):
    def get_template_names(self):
        return [self.kwargs.get('template_name') + ".html"]

    def get(self, request, *args, **kwargs):
        return super(SimpleStaticView, self).get(request, *args, **kwargs)


urlpatterns = [
    url(r'^api/', include('example.api.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^(?P<template_name>\w+)$',
        SimpleStaticView.as_view(), name='example'),
    url(r'^$', TemplateView.as_view(template_name='index.html')),
]
