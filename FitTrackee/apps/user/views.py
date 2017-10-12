from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate

from .forms import RegisterForm, ProfileForm
from ..activities.models import Activity


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
