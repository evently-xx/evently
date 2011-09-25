from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
  'ecal.views',        # the library to load functions 
  (r'^$', 'show_calendar'),  # the function to import
  (r'^(?P<year>\d+)-(?P<month>\d+)/(?P<change>prev|next)/$', 'show_calendar'),
  (r'^(?P<year>\d+)-(?P<month>\d+)$', 'show_calendar'),
  (r'^(?P<year>\d+)-(?P<month>\d+)-(?P<day>\d+)$', 'show_calendar_day'),
)

urlpatterns += patterns('',
  (r'^(?P<event_id>\d+)$', 'core.views.preview_event'),
) 
