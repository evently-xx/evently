# Create your views here.

from django.template import Context
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.http import Http404
from django.shortcuts import render_to_response


def foo(request):

  tmpl = get_template('home/dzhou.html')

  context = Context(
    {}
    )

  html = tmpl.render(context)

  return HttpResponse(html)
