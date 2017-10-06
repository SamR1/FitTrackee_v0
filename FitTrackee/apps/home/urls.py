from django.conf.urls import url

from . import views

app_name = 'home'
urlpatterns = [
    url(r'^home/', views.index, name='home'),
    url(r'^', views.index, name='home'),
]