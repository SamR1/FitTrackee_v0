from django.conf.urls import url

from . import views

app_name = 'user'
urlpatterns = [
    url(r'^edit/', views.edit, name='edit'),
    url(r'^', views.profile, name='profile'),
]
