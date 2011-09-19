# Create your views here.

from django.template import Context
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.http import Http404
from django.shortcuts import render_to_response

import settings
import sys
import os

def profile(request):

  tmpl = get_template('home/profile.html')

  context = Context(
    {"STATIC_URL" : os.path.join(settings.SITE_URL,
                                 settings.STATIC_URL)}

    )

  html = tmpl.render(context)

  return HttpResponse(html)
