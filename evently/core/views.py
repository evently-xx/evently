# Create your views here.

from django.template import Context
from django.http import HttpResponse
from django.template.loader import get_template


def preview_event(request, event_id):

  tmpl = get_template('core/preview_event.html')

  # fill in all fields of an event
  context = Context({'event_id' : event_id})

  html = tmpl.render(context)

  return HttpResponse(html)
