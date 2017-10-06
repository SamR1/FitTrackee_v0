from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate

from .forms import RegisterForm


def profile(request):
    return render(request, 'user/profile.html')


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
