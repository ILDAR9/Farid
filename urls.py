# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *
from django.conf import settings
from django.views.generic.simple import direct_to_template
# http://raphaeljs.com/
# mark down
# mercury editor
# Uncomment the next two lines to enable the admin:
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', direct_to_template, {'template': 'home.html'}),
    (r'^catalog$', direct_to_template, {'template': 'prise.html'})
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': './media/'}),
    )
