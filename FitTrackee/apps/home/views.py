from django.shortcuts import render

from ..activities.models import Activity


def index(request):
    friends_id = request.user.follows.all()
    users_list = [user.id for user in friends_id if user in friends_id]
    users_list.append(request.user.id)
    activities = Activity.objects.order_by('-activity_date').filter(user_id__in=users_list)[:20]
    return render(request, 'home/index.html', {'activities': activities})
