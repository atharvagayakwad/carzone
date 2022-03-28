from django.http import HttpResponse
from django.shortcuts import redirect, render
from cars.models import CarsModel
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.contrib import messages

from pages.models import TeamsModel

# Create your views here.


def home(request):
    # feature teams
    teams = TeamsModel.objects.all()

    # feature cars
    featured_cars = CarsModel.objects.order_by(
        '-created_date').filter(is_featured=True)

    # all cars
    all_cars = CarsModel.objects.order_by('-created_date')

    # search fields
    # this will give us all unique values and ignore the duplicates
    model_search = CarsModel.objects.values_list('model', flat=True).distinct()
    city_search = CarsModel.objects.values_list('city', flat=True).distinct()
    year_search = CarsModel.objects.values_list('year', flat=True).distinct()
    body_style_search = CarsModel.objects.values_list(
        'body_style', flat=True).distinct()

    context = {"teams": teams,
               'featured_cars': featured_cars, 'all_cars': all_cars, 'model_search': model_search, 'city_search': city_search, 'year_search': year_search, 'body_style_search': body_style_search}
    return render(request, 'pages/home.html', context)


def about(request):
    teams = TeamsModel.objects.all()
    context = {"teams": teams}
    return render(request, 'pages/about.html', context)


def services(request):
    return render(request, 'pages/services.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        phone = request.POST['phone']
        message = request.POST['message']

        email_subject = f'You have a new message from Carzone Website regarding {subject}'
        message_body = f"Name: {name}, Email: {email}, Phone: {phone}, Message: {message}"
        admin_info = User.objects.get(is_superuser=True)
        admin_email_id = admin_info.email

        send_mail(
            email_subject,
            message_body,
            'atharvag3011@gmail.com',
            [admin_email_id],
            fail_silently=False,
        )
        
        messages.success(request,
            'Thankyou for contacting us. We will get back to you shortly')
        return redirect('contact')
    return render(request, 'pages/contact.html')
