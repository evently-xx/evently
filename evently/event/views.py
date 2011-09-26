# Create your views here.

from django.template import Context, RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.http import Http404
from django.shortcuts import render_to_response
from django.contrib.comments.views.comments import post_comment

from core.models import Event

import time
from datetime import date, datetime, timedelta
import calendar

import settings
import os


def preview_event(request, event_id):
  try:
    event = Event.objects.get(pk = event_id)
  except Event.DoesNotExist:
    raise Http404

  # fill in all fields of an event
  context = RequestContext(
    request, {'event' : event}
    )

  return render_to_response("core/preview_event.html", context)


def preview_event_list(request):

  # get event ids
  maxEventNum = 100
  objs = Event.objects.all()
  eList = []
  for obj in objs:
    maxEventNum -= 1
    if maxEventNum <= 0:
      break

    eList.append(obj.eventID)

  # get template
  tmpl = get_template('core/preview_event_list.html')


  # fill in event list context
  context = Context(
    {'event_list' : eList}
    )

  html = tmpl.render(context)

  return HttpResponse(html)
