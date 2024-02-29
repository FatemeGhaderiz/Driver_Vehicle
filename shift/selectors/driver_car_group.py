from django.db.models import Q
from driver_vehicle_app.models import Appointment, CarsGroup, Car, CarGroup


def find_car_group(id):
     car = Car.objects.get(id = id)
     if CarsGroup.objects.filter(car = car).exists():
        car_group = CarsGroup.objects.get(car = car)
        return car_group.groupe.id
     return None
    



def driver_car_group_daily_shift(id, date, time):
    group_id = find_car_group(id)
    if group_id:
        car_group = CarGroup.objects.get(id=group_id)
        if car_group.daily_shift.filter(Q(date_start__lte=date) & Q(date_end__gte=date) & Q(time_start__lte=time) & Q(time_end__gte=time)).exists():
            car = Car.objects.get(id=id)
            object = Appointment.objects.get(Q(car=car) & Q(date_start__lte=date) & Q(date_end__gte=date))    
            return object.driver.id
        return None
            

   

def driver_car_group_weekly_shift(id, date, time):
      group_id = find_car_group(id)
      if group_id:
        car_group = CarGroup.objects.get(id=group_id)
        if car_group.weekly_shift.filter(Q(date_start__lte=date) & Q(date_end__gte=date) & Q(time_start__lte=time) & Q(time_end__gte=time)).exists():
            car = Car.objects.get(id=id)
            object = Appointment.objects.get(Q(car=car) & Q(date_start__lte=date) & Q(date_end__gte=date))    
            li = list(car_group.weekly_shift.days.split(","))
            day = date.weekday()
            if str(day) in li :
                return object.driver.id
            return None



def driver_car_group_monthly_shift(id, date, time):
    group_id = find_car_group(id)
    if group_id:
        car_group = CarGroup.objects.get(id=group_id)
        if car_group.weekly_shift.filter(Q(date_start__lte=date) & Q(date_end__gte=date) & Q(time_start__lte=time) & Q(time_end__gte=time)).exists():
            car = Car.objects.get(id=id)
            object = Appointment.objects.get(Q(car=car) & Q(date_start__lte=date) & Q(date_end__gte=date))    
            li = list(car_group.weekly_shift.days.split(","))
            day = date.day
            if str(day) in li :
                return object.driver.id
            return None