from django.conf.urls import url

from . import views

app_name = 'activities'
urlpatterns = [
    url(r'^add/', views.add_activity, name='add'),
    url(r'^(?P<activity_id>[0-9]+)$', views.display_activity),
    url(r'^', views.display_activities, name='index'),
]