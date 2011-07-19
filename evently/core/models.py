'''
data abstraction

@author dzhou
'''

__author__ = 'dzhou'


from django.db import models

class Event(models.Model):
  '''
  an event is the occasion, the idea, and the reasons for someone to
  organize an event
  '''

#  timeBegin = models.DateTimeField(db_index=True)
#  timeEnd = models.DateTimeField(db_index=True)
#  title = models.CharField(max_length=1024)
#  description = models.TextField()

  categoryID = models.CommaSeparatedIntegerField(db_index=True, max_length=512)
  datePosted = models.DateTimeField(null=True, blank=True, db_index=True)
  description = models.TextField(blank=True)
  distance = models.FloatField(db_index=True)
  distanceUnits = models.CharField(max_length=1024)
  endDate = models.DateField(null=True, blank=True, db_index=True)
  endTime = models.TimeField(null=True, blank=True, db_index=True)
  geoCodingAmbig = models.IntegerField()
  geoCodingPrec = models.CharField(max_length=1024)
  eventID = models.IntegerField(primary_key=True, db_index=True)
  latitude = models.FloatField(blank=True)
  longitude = models.FloatField(blank=True)
  metroID = models.CharField(blank=True, max_length=256)
  name = models.CharField(max_length=1024)
  numFutureEvents = models.IntegerField(blank=True, db_index=True)
  personal = models.IntegerField(blank=True, db_index=True)
  photoURL = models.URLField(blank=True, verify_exists=False)
  selfPromotion = models.IntegerField(blank=True)
  startDate = models.DateField(null=True, blank=True, db_index=True)
  startDateLastRendition = models.CharField(blank=True, max_length=512)
  startTime = models.TimeField(null=True, blank=True, db_index=True)
  ticketFree = models.IntegerField(null=True, blank=True, db_index=True)
  ticketPrice = models.CharField(blank=True, max_length=256)
  ticketURL = models.URLField(blank=True, verify_exists=False)
  URL = models.URLField(blank=True, verify_exists=False)
  userID = models.IntegerField(blank=True, db_index=True)
  utcEnd = models.DateTimeField(null=True, blank=True, db_index=True)
  utcStart = models.DateTimeField(null=True, blank=True, db_index=True)
  venueAddr = models.TextField(blank=True)
  venueCity = models.CharField(blank=True, db_index=True, max_length=256)
  venueCountryCode = models.CharField(blank=True, max_length=10)
  venueCountryID = models.IntegerField(blank=True, db_index=True)
  venueCountryName = models.CharField(blank=True, max_length=1024)
  venueID = models.IntegerField(blank=True, db_index=True)
  venueName = models.CharField(blank=True, max_length=1024)
  venueStateCode = models.CharField(blank=True, max_length=10)
  venueStateID = models.IntegerField(blank=True, db_index=True)
  venueStateName = models.CharField(blank=True, max_length=1024)
  venueZip = models.CharField(blank=True, db_index=True, max_length=32)
  watchListCount = models.IntegerField(blank=True, db_index=True)

  class Admin:
    pass


class Meetup(models.Model):
  '''
  a meetup is a gathering of friends to attend an event.
  it is a temporary association between a group of people with an event
  '''

  eventId = models.IntegerField()
  userIds = models.TextField() # better field type ?

  class Admin:
    pass
