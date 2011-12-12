'''
models for meet4fun, an light-weighted event organzier.

@author xliu
'''

__author__ = 'xliu'

from django.db import models
from django.contrib.auth.models import User

VISIBILITY = (
  ('p', 'public'),
  ('m', 'members'),
)

EVENT_STATUS = (
  ('u', 'upcoming'),
  ('p', 'past'),
  ('r', 'proposed'),
  ('s', 'suggested'),
)

RSVP_RESPONSE = ( 
  ('y', 'yes'),
  ('n', 'no'),
  ('m', 'maybe'),
  ('w', 'waitlist'),
)

# User are created as onetoone relation to the django build in user type.
# See why? https://docs.djangoproject.com/en/dev/topics/auth/
class UserProfile(models.Model):
  # one row in userprofile table corresponds to one user
  user = models.OneToOneField(User)
  # additional information should go from here.
  phone  = models.PhoneNumberField()

class Venue(models.Model):
  name = models.CharField(null=True, blank=True, max_length = 256)
  address_1 = models.CharField(null=True, blank=True, max_length=128)
  address_2 = models.CharField(null=True, blank=True, max_length=128)
  address_3 = models.CharField(null=True, blank=True, max_length=128)
  city = models.CharField(null=True, blank=True, max_length=64)
  state = models.CharField(null=True, blank=True, max_length=64)
  country = models.CharField(null=True, blank=True, max_length=64)
  zip = models.IntegerField(null=True, blank=True, db_index = True)
  lon = models.FloatField(null=True, db_index = True)
  lat = models.FloatField(null=True, db_index = True)
  phone = models.CharField(null=True, blank=True, max_length = 64)

class Event(models.Model):
  time = models.DateTimeField(null = True, blank = True, db_index=True)
  description = models.TextField(null=True, blank=True)
  visibility = models.CharField(null=True, blank=True, max_length = 1,
      choices=VISIBILITY)
  status = models.CharField(null=True, blank=True, max_length = 1,
      choices=EVENT_STATUS)
  venue = models.ForeignKey(Venue, null=True, blank=True, \
      on_delete=models.SET_NULL)
  hosts = models.ManyToManyField(User, related_name='user.hosted_events')
  participators = models.ManyToManyField(User, through="Rsvp",
      related_name='user.participated_events')

class Rsvp(models.Model):
  comment = models.TextField(null=True, blank=True)
  guest_count = models.IntegerField(null=True, blank=True, db_index = True)
  user = models.ForeignKey(User, null=True, blank=True, \
      on_delete=models.SET_NULL)
  event = models.ForeignKey(Event, null=True, blank=True, \
      on_delete=models.SET_NULL)  
  response = models.CharField(null=True, blank=True, max_length = 1,
      choices=RSVP_RESPONSE)
  created = models.DateTimeField(null = True, blank = True)
  updated = models.DateTimeField(null = True, blank = True)
  objects = RsvpManager() 
