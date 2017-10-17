from django.conf.urls import url

from . import views

app_name = 'user'
urlpatterns = [
    url(r'^delete/picture/', views.delete_picture, name='delete-avatar'),
    url(r'^edit/', views.edit, name='edit'),
    url(r'^(?P<user_id>[0-9]+)/addFriend/(?P<friend_id>[0-9]+)$', views.add_friend),
    url(r'^(?P<user_id>[0-9]+)/removeFriend/(?P<friend_id>[0-9]+)$', views.remove_friend),
    url(r'^(?P<user_id>[0-9]+)$', views.view_user),
    url(r'^', views.profile, name='profile'),
]
