from django.conf.urls import url

from . import views

app_name = 'activities'
urlpatterns = [
    url(r'^add/', views.add_activity, name='add'),
    url(r'^gpx/(?P<gpx_id>[0-9]+)/delete$', views.delete_activity),
    url(r'^(?P<activity_id>[0-9]+)/comment/(?P<comment_id>[0-9]+)/delete$', views.delete_comment),
    url(r'^(?P<activity_id>[0-9]+)/like$', views.like_activity),
    url(r'^(?P<activity_id>[0-9]+)$', views.display_activity),
    url(r'^$', views.display_activities, name='index'),
]