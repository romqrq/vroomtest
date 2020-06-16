from django.shortcuts import render
from .models import Car


def all_cars(request):
    """Function to display all cars into the search page"""
    cars = Car.objects.all()
    return render(request, "findcar.html", {"cars": cars})


def custom_classic_only(request):
    """Function to display only Custom Classic cars into the search page"""
    CS = []
    for car in Car.objects.all():
        if car.car_class == 'CS':
            CS.append(car)
    return render(request, "findcar.html", {"cars": CS})


def luxury_only(request):
    """Function to display only Luxury cars into the search page"""
    LX = []
    for car in Car.objects.all():
        if car.car_class == 'LX':
            LX.append(car)
    return render(request, "findcar.html", {"cars": LX})


def supersport_only(request):
    """Function to display only Supersport cars into the search page"""
    SS = []
    for car in Car.objects.all():
        if car.car_class == 'SS':
            SS.append(car)
    return render(request, "findcar.html", {"cars": SS})
