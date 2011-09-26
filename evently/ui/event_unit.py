from django.template import Context, RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.http import Http404
from django.shortcuts import render_to_response

def ui_render_event_unit(event):

  tmpl = get_template("ui/event_unit.html")
  c = Context({'event' : event});

  return tmpl.render(c);
