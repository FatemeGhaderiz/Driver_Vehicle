from django.db.models import Q
from driver_vehicle_app.models import Appointment,Car,CarsGroup,CarGroup

from .driver_car_group import driver_car_group_daily_shift,driver_car_group_weekly_shift,driver_car_group_monthly_shift,find_car_group


def driver_car_daily_shift(id, date, time):
    car = Car.objects.get(id=id)
    
    objects = Appointment.objects.filter(Q(car=car) & Q(date_start__lte=date) & Q(date_end__gte=date))

    for item in objects :
        if item.daily_shift.filter(Q(date_start__lte=date) & Q(date_end__gte=date) & Q(time_start__lte=time) & Q(time_end__gte=time)).exists():
            return item.driver.username
    return None    
   



def driver_car_weekly_shift(id, date, time):
    car = Car.objects.get(id=id)
    
    objects = Appointment.objects.filter(Q(car=car) & Q(date_start__lte=date) & Q(date_end__gte=date))

    day = date.weekday()
    print(day)

    for item in objects :
        if item.weekly_shift.filter(Q(date_start__lte=date) & Q(date_end__gte=date) & Q(time_start__lte=time) & Q(time_end__gte=time)).exists():
            ob = item.weekly_shift.get(Q(date_start__lte=date) & Q(date_end__gte=date) & Q(time_start__lte=time) & Q(time_end__gte=time))
            li = list(ob.days.split(","))
            if str(day) in li :
                return item.driver.username
    return None            
   



def driver_car_monthly_shift(id, date, time):
    car = Car.objects.get(id=id)
    
    objects = Appointment.objects.filter(Q(car=car) & Q(date_start__lte=date) & Q(date_end__gte=date))

    day = date.day

    for item in objects :
        if item.monthly_shift.filter(Q(date_start__lte=date) & Q(date_end__gte=date) & Q(time_start__lte=time) & Q(time_end__gte=time)).exists():
            ob = item.monthly_shift.get(Q(date_start__lte=date) & Q(date_end__gte=date) & Q(time_start__lte=time) & Q(time_end__gte=time))
            li = list(ob.days.split(","))
            if str(day) in li :
                return item.driver.username
    return None            





def driver_car_shift(id, date, time):
    result = {}

    driver_daily_shift = driver_car_daily_shift(id,date,time)    
    if driver_daily_shift:
        result["driver"] = driver_daily_shift

    driver_weekly_shift = driver_car_weekly_shift(id,date,time)    
    if driver_weekly_shift:
        result["driver"] = driver_weekly_shift

    driver_monthly_shift = driver_car_monthly_shift(id,date,time)    
    if driver_monthly_shift:
        result["driver"] = driver_monthly_shift




    driver_group_daily_shift = driver_car_group_daily_shift(id,date,time)    
    if driver_group_daily_shift:
        result["driver"] = driver_group_daily_shift

    driver_group_weekly_shift = driver_car_group_weekly_shift(id,date,time)    
    if driver_group_weekly_shift:
        result["driver"] = driver_group_weekly_shift

    driver_group_monthly_shift = driver_car_group_monthly_shift(id,date,time)    
    if driver_group_monthly_shift:
        result["driver"] = driver_group_monthly_shift

    return result