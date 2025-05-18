from django.db import models
from django.utils import timezone

# Create your models here.
class Car(models.Model):
    CAR_TYPE_CHOICE =[
        ('XL','SUV'),
        ('SE','SEDAN'),
        ('MINI','HATCHBACK'),
        ('CO','COUPE'),
        ('CONV','CONVERTIBLE')  
    ]
    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to='images/')
    date_added=models.DateTimeField(default=timezone.now)
    car_type=models.CharField(max_length=4,choices=CAR_TYPE_CHOICE)
    description=models.TextField(default='')

    def __str__(self):
        return self.name
