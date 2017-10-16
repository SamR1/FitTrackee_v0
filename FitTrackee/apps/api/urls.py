from django.conf.urls import url

from . import views

app_name = 'api'
urlpatterns = [
    url(r'^(?P<user_id>[0-9]+)/activities$', views.UserActivitiesList.as_view()),
    url(r'^activities/$', views.UserAllActivitiesList.as_view()),
]