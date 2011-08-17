
import os, sys
import urllib, sgmllib
from yelp_parsers import *
from core.models import YelpEvent

if __name__ == '__main__':
  website = 'http://www.yelp.com'
  event_link = '/events/larkspur-rose-and-pate-week-at-left-bank-brasseries-three-bay-area-locations'
  print 'Visiting: ' + website + event_link
  f = urllib.urlopen(website + event_link)
  s = f.read()
  # Try and process the page.
  # The class should have been defined first, remember.
  yelp_event = YelpEvent()
  yelp_event.eventURL = website + event_link
  yelp_eventpage_parser = YelpEventPageParser()
  yelp_eventpage_parser.parse(s, yelp_event)
  # Save Event to db:
  yelp_event.save()
  # Get the eventlinks.
  print yelp_event

