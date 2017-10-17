from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate

from .forms import RegisterForm, ProfileForm
from ..activities.models import Activity
from .models import User


@login_required
def profile(request):
    activities = Activity.objects.all().order_by('-activity_date').filter(
        user_id=request.user.id)[:5]
    return render(request, 'user/profile.html', {'activities': activities})


@login_required
def edit(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=request.user)
    return render(request, 'user/edit.html', {'form': form})


@login_required
def delete_picture(request):
    User.objects.get(id=request.user.id).picture.delete(save=True)
    return redirect('profile')


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home:home')
    else:
        form = RegisterForm()
    return render(request, 'user/register.html', {'form': form})


@login_required
def view_user(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    activities = Activity.objects.all().order_by('-activity_date').filter(
        user_id=user_id)[:5]
    return render(request, 'user/display_user.html', {'ft_user': user,
                                                      'activities': activities})
