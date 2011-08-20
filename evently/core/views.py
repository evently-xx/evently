# Create your views here.

from django.template import Context
from django.http import HttpResponse
from django.template.loader import get_template
from django.http import Http404

from core.models import Event

def preview_event(request, event_id):

  tmpl = get_template('core/preview_event.html')

  events = Event.objects.filter(eventID = event_id)
  if not len(events):
    raise Http404

  event = events[0]

  # fill in all fields of an event
  context = Context(
    {'event' : event}
    )

  html = tmpl.render(context)

  return HttpResponse(html)


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

