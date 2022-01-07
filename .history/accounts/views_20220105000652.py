from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.

def login(request):
    return render(request, 'accounts/login.html')

def register(request):
    if request.method == "POST":
        #messages.error(request, 'This is error message')
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirm_password = request.POST["confirm_password"]
        if password == confirm_password:
            if User.objects.filter(username=username).exists():

        else:
            messages.error(request, 'Password does\'t matched')
            return redirect("register")
    return render(request, 'accounts/register.html')

def dashboard(request):
    return render(request, 'accounts/dashboard.html')

def logout(request):
    return redirect('home')
