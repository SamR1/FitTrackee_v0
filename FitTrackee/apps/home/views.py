from django.shortcuts import render

from ..activities.models import Activity


def index(request):
    users_list = request.user.get_friends()
    users_list.append(request.user.id)
    activities = Activity.objects.order_by('-activity_date').filter(user_id__in=users_list)[:20]
    return render(request, 'home/index.html', {'activities': activities})
