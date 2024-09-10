from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import RegistrationForm
from django.contrib import messages
from django.shortcuts import render
from django.shortcuts import render
def register_view(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            user = User.objects.create_user(username = username, password = password, email = email)
            login(request, user)
            welcome_message = f"Hello {username}, welcome to Doctor Hub"
            messages.success(request, welcome_message)
            return redirect('home')
    else:
        form = RegistrationForm()
    return render(request, 'registration/accounts/register.html', {'form':form})


def login_view(request):
    error_message = None
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            welcome_message = f"Hello {username}, welcome to Doctor Hub"
            messages.success(request, welcome_message)
            return redirect('home')
        else:
            error_message = "Invalid Credentials!"
    return render(request, 'registration/accounts/login.html', {'error':error_message})


def logout_view(request):
        logout(request)
        return redirect('login')
    
