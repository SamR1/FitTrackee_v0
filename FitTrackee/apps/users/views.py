from django.shortcuts import render

from ..user.models import User


def index(request):
    users = User.objects.all().order_by('-date_joined')[:10]
    return render(request, 'users/display_users.html', {'ft_users': users})
