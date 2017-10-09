from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.db import transaction

from .models import Activity, Gpx, Sport
from ..user.models import User
from .forms import AddActivityForm
from .utils import gpx_info

from datetime import timedelta


@login_required
def add_activity(request):

    if request.method == 'POST':
        form = AddActivityForm(request.POST, request.FILES)
        if form.is_valid():

            try:
                with transaction.atomic():
                    user = User.objects.get(username=request.user.username)
                    sport = Sport.objects.get(pk=request.POST['sport'])

                    new_gpx = Gpx()
                    new_gpx.gpx_file = request.FILES['gpx_file']
                    new_gpx.save()

                    gpx_data = gpx_info(settings.MEDIA_ROOT + '/' + str(new_gpx.gpx_file))

                    new_activity = Activity()
                    new_activity.user = user
                    new_activity.sport = sport
                    new_activity.gpx = new_gpx
                    new_activity.activity_date = gpx_data['start']
                    new_activity.duration = timedelta(seconds=gpx_data['duration'])
                    new_activity.pauses = timedelta(seconds=gpx_data['stop_time'])
                    new_activity.moving = timedelta(seconds=gpx_data['moving_time'])
                    new_activity.distance = gpx_data['distance']
                    new_activity.min_alt = gpx_data['elevation_min']
                    new_activity.max_alt = gpx_data['elevation_max']
                    new_activity.descent = gpx_data['downhill']
                    new_activity.ascent = gpx_data['uphill']
                    new_activity.max_speed = gpx_data['max_speed']
                    new_activity.ave_speed = gpx_data['average_speed']

                    new_activity.save()

                    return redirect('/activities/' + str(new_activity.id))

            except Exception as e:
                print(e)
                err_msg = 'An error occurred, please retry'
                return render(request, 'activities/add_activity.html',
                              {'form': form, 'error': err_msg})

    else:
        form = AddActivityForm()
    return render(request, 'activities/add_activity.html',  {'form': form})


@login_required
def display_activity(request, activity_id):
    activity = get_object_or_404(Activity, pk=activity_id)
    return render(request, 'activities/display_activity.html', {'activity': activity})


@login_required
def display_activities(request):
    return render(request, 'activities/display_activities.html')
