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
    return render(request, 'pages/contact.html')
