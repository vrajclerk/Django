from django.urls import path
from . import views

urlpatterns = [
    path("", views.car, name="car"),
]
