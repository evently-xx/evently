#sys.path.append('../')

from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin

#from evently import urls

admin.autodiscover()

urlpatterns = patterns(
  'core.views',        # the library to load functions 
  # get list of objects
  (r'^$', 'preview_event_list'),
  # preview an object
  (r'^(?P<event_id>\d+)$', 'preview_event'),
)

