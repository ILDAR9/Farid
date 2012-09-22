# -*- coding: utf-8 -*-
from django.conf.urls import *
from django.conf import settings
from django.views.generic.simple import direct_to_template
urlpatterns = patterns('',
    url(r'^$', direct_to_template, {'template': 'home.html'}),
    url(r'^catalog$', direct_to_template, {'template': 'catalog.html'}),
    url(r'^prise-enter$', direct_to_template, {'template': 'prise_enter.html'}),
    url(r'^prise-parade$', direct_to_template, {'template': 'prise_parade.html'}),
    #url(r'^prise-lattice$', direct_to_template, {'template': 'prise_lattice.html'}),
    url(r'^prise-anti-fire$', direct_to_template, {'template': 'prise_anti_fire.html'}),
    url(r'^furnish$', direct_to_template, {'template': 'furnish.html'}),
    url(r'^color$', direct_to_template, {'template': 'color.html'}),
    url(r'^design', direct_to_template, {'template': 'design.html'}),
    url(r'^test$', direct_to_template, {'template': 'test.html'}),


    url(r'^rooms_door.files/sheet001.html$', direct_to_template, {'template': 'rooms_door.files/sheet001.html'}),
    url(r'^rooms_door.files/sheet002.html$', direct_to_template, {'template': 'rooms_door.files/sheet002.html'}),
    url(r'^rooms_door.files/sheet003.html$', direct_to_template, {'template': 'rooms_door.files/sheet003.html'}),
    url(r'^rooms_door.files/sheet004.html$', direct_to_template, {'template': 'rooms_door.files/sheet004.html'}),
    url(r'^rooms_door.files/sheet005.html$', direct_to_template, {'template': 'rooms_door.files/sheet005.html'}),
    url(r'^rooms_door.files/sheet006.html$', direct_to_template, {'template': 'rooms_door.files/sheet006.html'}),
    url(r'^rooms_door.files/sheet007.html$', direct_to_template, {'template': 'rooms_door.files/sheet007.html'}),
     # url(r'^rooms_door.files/sheet008.html$', direct_to_template, {'template': 'sheet008.html'}),
    url(r'^arch$', direct_to_template, {'template': 'arch.html'}),
    url(r'^rooms_door.files/sheet009.html$', direct_to_template, {'template': 'rooms_door.files/sheet009.html'}),
    url(r'^rooms_door.files/sheet010.html$', direct_to_template, {'template': 'rooms_door.files/sheet010.html'}),
    url(r'^rooms_door.files/sheet011.html$', direct_to_template, {'template': 'rooms_door.files/sheet011.html'}),
    url(r'^rooms_door.files/sheet012.html$', direct_to_template, {'template': 'rooms_door.files/sheet012.html'}),    
    url(r'^rooms_door.files/tabstrip.html$', direct_to_template, {'template': 'rooms_door.files/tabstrip.html'}),
    
)



if settings.DEBUG:
    urlpatterns += patterns('',
        (r'media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': './media/'}),
    )