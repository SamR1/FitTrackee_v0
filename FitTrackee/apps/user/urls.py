from django.conf.urls import url

from . import views

app_name = 'user'
urlpatterns = [
    url(r'^profile/', views.profile, name='profile'),
]