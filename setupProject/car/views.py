from django.shortcuts import render
from .models import Car
from django.shortcuts import get_object_or_404

# Create your views here.
def car(request):
    cars=Car.objects.all()
    return render(request, 'car/car.html',{'cars':cars})

def car_detail(request, car_id):
    car=get_object_or_404(Car, pk=car_id)
    return render(request, 'car/car_detail.html', {'car': car})