from django.shortcuts import get_object_or_404, render

from cars.models import CarsModel
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

# Create your views here.
def cars(request):
    cars = CarsModel.objects.order_by('-created_date')

    paginator = Paginator(cars, 2)
    page = request.GET.get('page')
    paged_cars = paginator.get_page(page)

    model_search = CarsModel.objects.values_list('model', flat=True).distinct()
    city_search = CarsModel.objects.values_list('city', flat=True).distinct()
    year_search = CarsModel.objects.values_list('year', flat=True).distinct()
    body_style_search = CarsModel.objects.values_list(
        'body_style', flat=True).distinct()

    context = {'cars': paged_cars, 'model_search': model_search, 'city_search': city_search, 'year_search': year_search, 'body_style_search': body_style_search}
    return render(request, 'cars/cars.html', context)

def car_detail(request,id):
    single_car = get_object_or_404(CarsModel,pk=id)

    context = {'single_car':single_car}
    return render(request, 'cars/car_detail.html', context)

def search(request):
    cars = CarsModel.objects.order_by('-created_date')

    model_search = CarsModel.objects.values_list('model', flat=True).distinct()
    city_search = CarsModel.objects.values_list('city', flat=True).distinct()
    year_search = CarsModel.objects.values_list('year', flat=True).distinct()
    body_style_search = CarsModel.objects.values_list(
        'body_style', flat=True).distinct()
    transmission_search =CarsModel.objects.values_list('transmission', flat=True).distinct()

    # if we have 'keyword' in url then 
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']

        # if keyword is not blank
        if keyword:
            cars = cars.filter(description__icontains=keyword)

    # if we have 'model' in url then get its value
    if 'model' in request.GET:
        model = request.GET['model']

        # if model is not blank
        if model:
            cars = cars.filter(model__iexact=model) # and match it will the exact value in database

    if 'city' in request.GET:
        city = request.GET['city']

        # if city is not blank
        if city:
            cars = cars.filter(city__iexact=city) # and match it will the exact value in database

    if 'year' in request.GET:
        year = request.GET['year']

        # if year is not blank
        if year:
            cars = cars.filter(year__iexact=year) # and match it will the exact value in database
    
    if 'body_style' in request.GET:
        body_style = request.GET['body_style']

        # if body_style is not blank
        if body_style:
            cars = cars.filter(body_style__iexact=body_style) # and match it will the exact value in database

    if 'min_price' in request.GET:
        min_price = request.GET['min_price']
        max_price = request.GET['max_price']

        if max_price:
            cars = cars.filter(price__gte=min_price, price__lte=max_price)

    context = {'cars': cars, 'model_search': model_search, 'city_search': city_search, 'year_search': year_search, 'body_style_search': body_style_search,'transmission_search':transmission_search}
    return render(request, 'cars/search.html',context)