from .models import Alumn
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password')
            return redirect('login')
    else:
        return render(request, 'authentication/login.html')


def logout_view(request):
    logout(request)
    return redirect('login')


def alumni_list(request):
    alumni = Alumn.objects.all()
    return render(request, 'alumni_list.html', {'alumni': alumni})


def alum_profile(request, id):
    alum = Alumn.objects.get(id=id)
    return render(request, 'alum_profile.html', {'alum': alum})
