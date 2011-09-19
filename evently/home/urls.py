from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

print "hello world"

urlpatterns = patterns(
  'home.views',
  (r'^$', 'foo'),
)
