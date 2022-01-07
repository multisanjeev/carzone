from django.shortcuts import render

# Create your views here.

def login(request):
    return render(request, 'accouunts/login.html')

def register(request):
    return render(request, 'accounts/register.html')
