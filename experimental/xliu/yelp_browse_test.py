import urllib
from yelp_parsers import YelpBrowseParser, YelpDirectoryParser

dir_url = 'http://www.yelp.com/locations?return_url=%2Fevents'
print 'Visiting: ' + dir_url
f = urllib.urlopen(dir_url)
s = f.read()
# Try and process the page.
# The class should have been defined first, remember.
yelp_dir_parser = YelpDirectoryParser()
yelp_dir_parser.parse(s)
# Get the eventlinks.
browse_city_links = yelp_dir_parser.get_city_links()

print browse_city_links

'''
website = 'http://www.yelp.com'
browse_dir = '/events/alameda-ca/browse'
event_links = []
while browse_dir != None:
  print 'Visiting: ' + website + browse_dir
  f = urllib.urlopen(website + browse_dir)
  s = f.read()
  # Try and process the page.
  # The class should have been defined first, remember.
  yelp_browse_parser = YelpBrowseParser()
  yelp_browse_parser.parse(s)
  # Get the eventlinks.
  event_links.append(yelp_browse_parser.get_eventlinks())
  browse_dir = yelp_browse_parser.get_next_browse_link()
  print event_links
  print browse_dir
'''
