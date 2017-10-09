from django.conf.urls import url

from . import views

app_name = 'activities'
urlpatterns = [
    url(r'^add/', views.add_activities, name='add'),
    url(r'^', views.display_activities, name='index'),
]