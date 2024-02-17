from django.db import models
from django.utils.timezone import now


# Create your models here.

class CarMake(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    def __str__(self):
        return self.name 


class CarModel(models.Model):
    carmake = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    name = models.CharField(null=False, max_length=50)
    id = models.IntegerField(default=1, primary_key=True)
        
    SEDAN = 'Sedan'
    SUV = 'SUV'
    WAGON = 'Wagon'
    CAR_TYPES = [
        (SEDAN, 'Sedan'),
        (SUV, 'SUV'),
        (WAGON, 'Wagon'),
    ]

    car_type = models.CharField(null=False, max_length=50, choices=CAR_TYPES)
    year = models.DateField(default=now)
    def __str__(self):
        return "Name: " + self.name + "," + \
            "Type: " + self.car_type


# <HINT> Create a plain Python class `CarDealer` to hold dealer data


# <HINT> Create a plain Python class `DealerReview` to hold review data
