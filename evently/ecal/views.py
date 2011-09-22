# Create your views here.

from django.template import Context, RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.http import Http404
from django.shortcuts import render_to_response

import sys

from core.models import Event

import time
from datetime import date, datetime, timedelta
import calendar

import settings
import os


mnames = "January February March April May June July August September October November December"
mnames = mnames.split()


def show_calendar(request, year=None, month=None, change=None):
  """Listing of days in `month`."""
  if year == None or month == None:
    now = datetime.now()
    year = now.year
    month = now.month
    today = now.day
  else:
    year, month = int(year), int(month)
    today = -1

  print year, month, today, change

  # apply next / previous change
  if change in ('next', 'prev'):
    now, mdelta = date(year, month, 15), timedelta(days=31)
    if change == 'next':
      mod = mdelta
    elif change == 'prev':
      mod = -mdelta

    year, month = (now+mod).timetuple()[:2]

  # init variables
  cal = calendar.Calendar()
  month_days = cal.itermonthdays(year, month)
  nyear, nmonth, nday = time.localtime()[:3]
  lst = [[]]
  week = 0

  # make month lists containing list of days for each week
  # each day tuple will contain list of entries and 'current' indicator
  for day in month_days:
    entries = current = False   # are there entries for this day; current day?
    if day:
      #entries = Entry.objects.filter(date__year=year, date__month=month, date__day=day)
      entries = Event.objects.filter(datePosted__year=year, datePosted__month=month, datePosted__day=day, eventID__exact=-111)
      if day == nday and year == nyear and month == nmonth:
        current = True

    lst[week].append((day, entries, current))
    if len(lst[week]) == 7:
      lst.append([])
      week += 1

  return render_to_response("ecal/calendar.html",
                            dict(year=year,
                                 month=month,
                                 user=None,
                                 month_days=lst,
                                 mname=mnames[month-1],
                                 static_url=os.path.join(settings.SITE_URL,
                                                         settings.STATIC_URL)))


def show_calendar_day(request, year, month, day):
  """Listing of events in 'day'."""

  year, month, day = int(year), int(month), int(day)

  entries = Event.objects.filter(datePosted__year=year,
                                 datePosted__month=month,
                                 datePosted__day=day)

  print len(entries)

  return render_to_response("ecal/calendar_oneday.html",
                            dict(year=year,
                                 month=month,
                                 day=day,
                                 user=None,
                                 mname=mnames[month-1],
                                 event_list=entries))

