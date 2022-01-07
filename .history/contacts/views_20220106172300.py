from django.shortcuts import render
from .models import Contact
from django.contrib import messages

# Create your views here.

def inquiry(request):
    if request.method == "POST":
        car_id = request.POST["car_id"]
        car_title = request.POST["car_title"]
        user_id = request.POST["user_id"]
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        customer_need = request.POST["customer_need"]
        city = request.POST["city"]
        state = request.POST["state"]
        email = request.POST["email"]
        message = request.POST["message"]
        phone = request.POST["phone"]

        contact = Contact(car_id=car_id, car_title=car_title, user_id=user_id,first_name=first_name,
        last_name=last_name, customer_need=customer_need, city=city, state=state, email=email, 
        message=message, phone=phone)
        contact.save()

        messages.success(request, 'you request has been submitted successfully, we will connect to you shortly')
        
    return