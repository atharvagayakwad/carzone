from django.http import HttpResponse
from django.shortcuts import render
from cars.models import CarsModel

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

    context = {"teams": teams,
               'featured_cars': featured_cars, 'all_cars': all_cars}
    return render(request, 'pages/home.html', context)


def about(request):
    teams = TeamsModel.objects.all()
    context = {"teams": teams}
    return render(request, 'pages/about.html', context)


def services(request):
    return render(request, 'pages/services.html')


def contact(request):
    return render(request, 'pages/contact.html')
