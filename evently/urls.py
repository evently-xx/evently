from django.conf.urls.defaults import *

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

    # preview a calendar
    (r'^preview/calendar/(?P<year>\d+)-(?P<month>\d+)/(?P<change>prev|next)/$', 'core.views.preview_calendar'),
    (r'^preview/calendar/(?P<year>\d+)-(?P<month>\d+)$', 'core.views.preview_calendar'),
    (r'^preview/calendar/$', 'core.views.preview_calendar'),

    (r'^preview/calendar_day/(?P<year>\d+)-(?P<month>\d+)-(?P<day>\d+)$', 'core.views.preview_calendar_day'),

    # Uncomment the admin/doc line below to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),

)
