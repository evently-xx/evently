from django.template import Context, RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.http import Http404
from django.shortcuts import render_to_response

import os
import settings

def ui_render_event_unit(event):

  tmpl = get_template("ui/event_unit.html")
  c = Context({
    'event' : event,
    'static_url' : os.path.join(settings.SITE_URL, settings.STATIC_URL)
  });

  return tmpl.render(c);
