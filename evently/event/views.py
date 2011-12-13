from django.template import Context, RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.http import Http404
from django.shortcuts import get_object_or_404, render_to_response
from django.core.urlresolvers import reverse
from models import Event, EventForm

__author__ = 'xliu'

# The handler to create a event form EventForm
def create(request):
  if request.method == 'POST': # If the form has been submitted...
    form = EventForm(request.POST) # A form bound to the POST data
    if form.is_valid(): # All validation rules pass
      #TODO(xingjie): Process the data in form.cleaned_data
      new_event = form.save()
      return HttpResponseRedirect(reverse('event.views.preview', args=(new_event.id,))) # Redirect after POST
  else:
    form = EventForm() # An unbound form

  return render_to_response('event/create.html', {'form': form},\
      context_instance=RequestContext(request))

def preview(request, event_id):
  event = get_object_or_404(Event.objects.get(pk=1))
  return render_to_response("event/preview.html", {'event' : event})


def preview_list(request):

  # get event ids
  # TODO(Xingjie): Simply and update this code, 
  maxEventNum = 100
  objs = Event.objects.all()
  eList = []
  for obj in objs:
    maxEventNum -= 1
    if maxEventNum <= 0:
      break

    eList.append(obj.id)

  # get template
  tmpl = get_template('event/preview_list.html')


  # fill in event list context
  context = Context(
    {'event_list' : eList}
    )

  html = tmpl.render(context)

  return HttpResponse(html)
