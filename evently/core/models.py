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

  timeBegin = models.DateTimeField(db_index=True)
  timeEnd = models.DateTimeField(db_index=True)
  title = models.CharField(max_length=1024)
  description = models.TextField()

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
