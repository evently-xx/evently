# Create your views here.

from django.template import Context
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.http import Http404
from django.shortcuts import render_to_response
from django.template import RequestContext

import settings
import sys
import os

def profile(request):

  tmpl = get_template('home/profile.html')

  c = RequestContext(
    request,
    {}
    )

  print c

  html = tmpl.render(c)

  return HttpResponse(html)
