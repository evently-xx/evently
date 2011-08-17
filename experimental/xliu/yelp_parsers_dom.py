import os, sys
sys.path.append('../') 
sys.path.append('../../') 
import urllib
import time
import datetime
#from xml.dom.minidom import parseString
import libxml2dom

from django.core.management import setup_environ
from evently import settings
setup_environ(settings)
from core.models import YelpEvent

# A parser to parse a paticular event page of yelp.com
class YelpEventPageParser():
  "A parser class configured to parse the event page of yelp.com"

  def parse(self, s, yelp_event):
    #page_node = parseString(s)
    page_node = libxml2dom.parseString(s, html=1)
    #print page_node
    event_node = self.find_main_event(page_node)
    self.parse_event(self, event_node)

  def find_main_event(node):
    if node.tagName == 'div' and node.attributes['id'] == 'main_events':
      return node
    for child_node in node.childNodes:
      found = find_main_event(child_node)
      if found != None:
        return found
    return None

  def parse_event(self, node):
    for child_node in node.childNodes:
      if child_node.tagName == 'div' and node.attributes['id'] == 'event_details_photos':
        parse_photo_tag(self, child_node)
      elif child_node.tagName == 'h1' and node.attributes['id'] == 'event_name':
        parse_event_name(self, child_node)
      elif child_node.tagName == 'dl' and node.attributes['class'] == 'event_item':
        parse_event_item(self, child_node)

  def parse_photo_tag(self, node):
    for child_node in node.childNodes:
      if child_node.tagName == 'a' and node.attributes['id'] == 'main_event_photo':
        self.yelp_event.photoURL = node.attributes['href'];
    
  def parse_event_name(self, node):
    assert node.nodeType == node.TEXT_NODE
    self.yelp_event.name = node.nodeValue

  def parse_event_item(self, node):
    for child_node in node.childNodes:
      if child_node.tagName == 'dt':
        assert child_node.nodeType == node.TEXT_NODE
        item_type = child_node.nodeValue;
      elif child_node.tagName == 'dd':
        if item_type == "Category:":
          parse_category(self, child_node)
        elif item_type == "When:":
          parse_time(self, child_node)
        elif item_type == "Where:":
          parse_addr(self, child_node)
        elif item_type == "How:":
          parse_how(self, child_node)
        elif item_type == "Cost:":
          parse_cost(self, child_node)
        elif item_type == "What/Why:":
          parse_description(self, child_node)

  def parse_category(self, node):
    for child_node in node.childNodes:
      assert child_node.tagName == 'a'
      assert child_node.nodeType == child_node.TEXT_NODE
      self.yelp_event.category = child_node.nodeValue

  def parse_time(self, node):
    for child_node in node.childNodes:
      if child_node.tagName == 'abbr':
        if child_node.attributes['class'] == 'dtstart':
          self.yelp_event.utcStart = dateutil.parser.parse(
              child_node.attributes['title'])
        elif child_node.attributes['class'] == 'dtend':
          self.yelp_event.utcEnd = dateutil.parser.parse(
              child_node.attributes['title'])
         
  def parse_addr(self, node):
    addr_nodes = node.getElementsByTagName('address')
    for addr_node in addr_nodes:
      self.yelp_event.venuePhone = addr_node.nodeValue
      for child_node in addr_node.childNodes:
        if child_node.tagName == 'span':
          if child_node.attributes['class'] == 'street-address':
            self.yelp_event.venueAddr = child_node.nodeValue
          elif child_node.attributes['class'] == 'locality':
            self.yelp_event.venueCity = child_node.nodeValue
          elif child_node.attributes['class'] == 'region':
            self.yelp_event.venueStateName = child_node.nodeValue
          elif child_node.attributes['class'] == 'postal-code':
            self.yelp_event.venueZip = child_node.nodeValue

  def parse_how(self, node):
    for child_node in node.childNodes:
      assert child_node.tagName == 'a'
      self.yelp_event.howHerf = child_node.attributes['href']

  def parse_cost(self, node):
    self.yelp_event.cost = node.nodeValue

  def parse_desc(self, node):
    assert node.tagName == 'dd' and node.attributes['class'] == 'event_description'
    self.yelp_event.description = node.nodeValue
