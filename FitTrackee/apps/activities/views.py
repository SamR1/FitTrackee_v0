from django.shortcuts import render

# from .models import Activity, Gpx, Sport


def add_activities(request):
    return render(request, 'activities/add_activity.html')


def display_activities(request):
    return render(request, 'activities/display_activities.html')
