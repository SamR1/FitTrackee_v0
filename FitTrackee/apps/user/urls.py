from django.conf.urls import url

from . import views

app_name = 'user'
urlpatterns = [
    url(r'^delete/picture/', views.delete_picture, name='delete-avatar'),
    url(r'^edit/', views.edit, name='edit'),
    url(r'^', views.profile, name='profile'),
]
