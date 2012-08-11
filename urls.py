# -*- coding: utf-8 -*-
from django.conf.urls import *
from django.conf import settings
from django.views.generic.simple import direct_to_template


urlpatterns = patterns('',
    url(r'^$', direct_to_template, {'template': 'home.html'}),
    url(r'^catalog$', direct_to_template, {'template': 'catalog.html'}),
    url(r'^prise-enter$', direct_to_template, {'template': 'prise_enter.html'}),
    url(r'^prise-parade$', direct_to_template, {'template': 'prise_parade.html'}),
    url(r'^prise-lattice$', direct_to_template, {'template': 'prise_lattice.html'}),
    url(r'^color', direct_to_template, {'template': 'color.html'}),

)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': './media/'}),
    )
