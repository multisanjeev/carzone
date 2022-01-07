from django.shortcuts import render, redirect
from .models import Contact
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.models import User

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

        if request.user.is_authenticated:
            has_contacted = Contact.objects.all().filter(car_id=car_id, user_id=user_id)
            if has_contacted:
                messages.error(request, 'you have already made an inquiry about this car, please wait until we get back to you.')
                return redirect('/cars/'+ car_id)

        contact = Contact(car_id=car_id, car_title=car_title, user_id=user_id,first_name=first_name,
        last_name=last_name, customer_need=customer_need, city=city, state=state, email=email, 
        message=message, phone=phone)

        admin_info = User.objects.get(is_superuser=True)
        admin_email = admin_info.email
        send_mail(
                'New Car inquiry',
                'You hava an inquiry for the car' + car_title,
                'sanjeev.katiyar2@gmail.com',
                [admin_email],
                fail_silently=False,
            )
        contact.save()

        messages.success(request, 'you request has been submitted successfully, we will connect to you shortly')
        return redirect('/cars/'+car_id)
        
    return