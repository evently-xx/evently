from django.conf.urls.defaults import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^evently/', include('evently.foo.urls')),

    # get list of objects
    (r'^preview/event/$', 'core.views.preview_event_list'),

    # preview an object
    (r'^preview/event/(?P<event_id>\d+)$', 'core.views.preview_event'),

    # Uncomment the admin/doc line below to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    
    # preview a comments	
    (r'^comments/', include('django.contrib.comments.urls')),

    # home page
    (r'^profile/', include('home.urls')),

    # Event page
    (r'^event/', include('event.urls')),

    # calendar
    (r'^calendar/', include('ecal.urls')),
    #(r'^calendar/(?P<year>\d+)-(?P<month>\d+)/(?P<change>prev|next)/$',
    #                 include('ecal.urls')),
    #(r'^calendar/(?P<year>\d+)-(?P<month>\d+)$', include('ecal.urls')),

    # serve static files
#    (r'^%s(.*)$' % settings.STATIC_URL, 'django.views.static.serve',
#       {'document_root': settings.STATIC_ROOT,
#        'show_indexes' : True}),

)

# serve static files
urlpatterns += staticfiles_urlpatterns()

