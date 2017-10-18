"""FitTrackee URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.contrib.auth.decorators import user_passes_test

from FitTrackee import settings
from apps.user import views as user_view
from apps.home import views as home_view

login_forbidden = user_passes_test(lambda u: u.is_anonymous(), '/home')
anonymous_forbidden = user_passes_test(lambda u: u.is_authenticated(), '/login')

urlpatterns = [
    url(r'^login/$', login_forbidden(auth_views.login), name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/login'}, name='logout'),
    url(r'^register/$', login_forbidden(user_view.register), name='register'),
    url(r'^users/', include('apps.users.urls')),
    url(r'^user/', include('apps.user.urls')),
    url(r'^activities/', include('apps.activities.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^home/',  include('apps.home.urls')),
    url(r'^profile/$', user_view.profile, name='profile'),
    url(r'^api/', include('apps.api.urls')),
    url(r'^$', anonymous_forbidden(home_view.index)),
] + static(settings.STATIC_URL)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
