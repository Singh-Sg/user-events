import json
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Event
from .forms import EventForm


def pagination(request, queryset):
    page = request.GET.get('page', settings.FIRST_PAGE)
    paginator = Paginator(queryset, settings.NUM_OF_OBJECTS)
    try:
        events = paginator.page(page)
    except PageNotAnInteger:
        events = paginator.page(settings.FIRST_PAGE)
    except EmptyPage:
        events = paginator.page(paginator.num_pages)
    return events


@login_required
def index(request):
    """
    Show all events order by latest
    """
    all_events = Event.objects.all().order_by('-id')
    events = pagination(request, all_events)
    return render(request, 'index.html', {'events': events, 'user': request.user})


@login_required
def create_event(request):
    """
    Create events
    """
    if request.method == 'POST':
        form = EventForm(request.POST, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('my_events')
    else:
        form = EventForm()
    return render(request, 'create-event.html', {'form': form})


@login_required
def update_event(request, pk):
    """
    Update events
    """
    event = get_object_or_404(Event, pk=pk)
    if request.user == event.user:
        form = EventForm(request.POST or None, instance=event)
        if form.is_valid():
            form.save()
            return redirect('my_events')
        return render(request, 'create-event.html', {'form': form})
    return redirect('index')


@login_required
def delete_event(request, pk):
    """
    Delete events
    """
    event = get_object_or_404(Event, pk=pk)
    if request.user == event.user:
        event.delete()
        return redirect('my_events')
    return redirect('index')


@login_required
def my_events(request):
    """
    Show logged in user's created events
    """
    my_events = Event.objects.filter(user=request.user).order_by('-id')
    events = pagination(request, my_events)
    return render(request, 'myevents.html', {'events': events})


@login_required
def join_event(request):
    """
    Join users in events
    """
    if request.is_ajax():
        event_id = request.GET.get('envetId')
        events = get_object_or_404(Event, pk=event_id)
        events.participants.add(request.user)
        events.save()
        context_dict = {'success': "success", 'status': 200}
    else:
        context_dict = {'errors': "Bad Request", 'status': 400}
    return HttpResponse(json.dumps(context_dict), content_type="application/json")
