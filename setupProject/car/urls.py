from django.urls import path
from . import views

urlpatterns = [
    path("", views.car, name="car"),
    path("<int:car_id>/", views.car_detail, name="car_detail"),
]
