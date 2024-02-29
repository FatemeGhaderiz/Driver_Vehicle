from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from shift.models import DailyShift,WeeklyShift,MonthlyShift

class Driver(models.Model):
    username = models.CharField(max_length=255)
    code = models.CharField(max_length=10)
 
    
class DriverGroup(models.Model):
    name = models.CharField(max_length=255)
    daily_shift = GenericRelation(DailyShift)
    weekly_shift = GenericRelation(WeeklyShift)
    monthly_shift = GenericRelation(MonthlyShift)

class DriversGroup(models.Model):
    driver = models.ForeignKey('Driver', on_delete=models.CASCADE)
    groupe = models.ForeignKey('DriverGroup', on_delete=models.CASCADE)





class Car(models.Model):
    model = models.CharField(max_length=255)
    license_plate = models.CharField(max_length=20 , unique = True)


class CarGroup(models.Model):
    name = models.CharField(max_length=255 , unique = True)
    daily_shift = GenericRelation(DailyShift)
    weekly_shift = GenericRelation(WeeklyShift)
    monthly_shift = GenericRelation(MonthlyShift)


class CarsGroup(models.Model):
    car = models.ForeignKey('Car', on_delete=models.CASCADE)
    groupe = models.ForeignKey('CarGroup', on_delete=models.CASCADE)





class Appointment(models.Model):
    car = models.ForeignKey('Car', on_delete=models.CASCADE)
    driver = models.ForeignKey('Driver', on_delete=models.CASCADE)
    date_start = models.DateField()
    date_end = models.DateField()
    daily_shift = GenericRelation(DailyShift)
    weekly_shift = GenericRelation(WeeklyShift)
    monthly_shift = GenericRelation(MonthlyShift)
    




