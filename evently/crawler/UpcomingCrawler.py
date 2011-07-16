#!/usr/bin/env python

import os, sys
import urllib
import json
import time

class UpcomingCrawler:
    '''
    The class to collect data (events) from Web
    '''

    # Attributes
    api_key = ''
    api_method = ''
    api_query = 'http://upcoming.yahooapis.com/services/rest/'

    def __init__(self):
        self.api_key = ''
        self.api_method = ''
        return

    def set_api_key(self, api_key):
        self.api_key = api_key
        return

    def set_api_method(self, api_method):
        self.api_method = api_method
        return

    def event_search(self, location):
        '''
        search 100 public events near the specific location
        Param:
            location : string
        Return:
            event_list: a list of events, each of which is represented by \
                        a dict object. All events are sorted based on distance
        '''
        get_query = '%s?api_key=%s&method=%s&location=%s&format=json' \
                    % (self.api_query, \
                       self.api_key, \
                       self.api_method, \
                       urllib.quote(location, '/,'))
        res_stream = urllib.urlopen(get_query)
        res_data = json.load(res_stream)
        event_list = res_data['rsp']['event']
        print "Successfully crawling %d events" % (len(event_list))
        return event_list

    def daily_event_search(self, location):
        search_count = 0
        while True:
            print search_count
            self.event_search(location)
            search_count = search_count + 1
            if search_count >= 5:
                break
            time.sleep(10)


if __name__ == '__main__':
    dc = UpcomingCrawler()
    dc.set_api_key('6b6117dc75')
    dc.set_api_method('event.search')
    dc.event_search('san francisco, ca')
    #dc.daily_event_search('san francisco, ca')
