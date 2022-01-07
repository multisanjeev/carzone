from django.shortcuts import render, redirect
from django.contrib import messages

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
    return render(request, 'accounts/register.html')

def dashboard(request):
    return render(request, 'accounts/dashboard.html')

def logout(request):
    return redirect('home')
