from django.db.models import Q
import datetime
from ..models import DailyShift, WeeklyShift, MonthlyShift
from driver_vehicle_app.models import Driver,DriversGroup,DriverGroup,Appointment,Car,CarGroup,CarsGroup
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import  get_object_or_404



def object_shift(date,id,model):
    
    result = {}

    try :
        object = model.objects.get(id = id)

        if object.daily_shift.filter(Q(date_start__lte=date) & Q(date_end__gte=date)).exists():
            daly_shift = object.daily_shift.get(Q(date_start__lte=date) & Q(date_end__gte=date))
            daily_time ={
                        "time_start" : daly_shift.time_start,
                        "time_end" : daly_shift.time_end
                    }
            result["daily_shift"] = daily_time


        if object.weekly_shift.filter(Q(date_start__lte=date) & Q(date_end__gte=date)).exists():
            weekly_shift = object.weekly_shift.get(Q(date_start__lte=date) & Q(date_end__gte=date))
            if weekly_shift :
                li = list(weekly_shift.days.split(","))
                week_day = date.weekday()
                if str(week_day) in li :
                    weekly_time ={
                            "time_start" : weekly_shift.time_start,
                            "time_end" : weekly_shift.time_end
                        }
                    result["weekly_shift"] = weekly_time
            

        if object.monthly_shift.filter(Q(date_start__lte=date) & Q(date_end__gte=date)).exists():
            month_shift = object.monthly_shift.get(Q(date_start__lte=date) & Q(date_end__gte=date))
            if month_shift :
                li = list(month_shift.days.split(","))
                month_day = date.day
                print(month_day)
                if str(month_day) in li :
                    monthly_time ={
                            "time_start" : month_shift.time_start,
                            "time_end" : month_shift.time_end
                        }
                    result["month_shift"] = monthly_time

        return result        

    except model.DoesNotExist:    
        return None


    
   
       

def find_driver_appoiment(id,date):
     driver = Driver.objects.get(id = id)
     if Appointment.objects.filter(Q(driver = driver)& Q(date_start__lte=date) & Q(date_end__gte=date)).exists():
        appointment = Appointment.objects.get(Q(driver = driver)
        & Q(date_start__lte=date) & Q(date_end__gte=date))

        return appointment.id
     else:
         return None





def find_driver_group(id):
     diver = Driver.objects.get(id = id)
     if DriversGroup.objects.filter(driver = diver).exists():
        driver_group = DriversGroup.objects.get(driver = diver)
        return driver_group.groupe.id
     return None
    



def find_car_group(id,date):
    driver = Driver.objects.get(id = id)
    appointment = Appointment.objects.get(Q(driver = driver)
    & Q(date_start__lte=date) & Q(date_end__gte=date))

    car = appointment.car

    if CarsGroup.objects.filter(car = car).exists():
        car_group = CarsGroup.objects.get(car = car)
        return car_group.groupe.id
    return None

     




def shift_object(id,date):
    result = {}
    driver_group_id = find_driver_appoiment(id,date)    
    if driver_group_id:
        driver_appointment_shift = object_shift(date,driver_group_id,Appointment)
        if driver_appointment_shift:
            result["driver_shift"] = driver_appointment_shift

    driver_group_id = find_driver_group(id)    
    if driver_group_id:
        driver_group_shift = object_shift(date,driver_group_id,DriverGroup)
        if driver_group_shift:
            result["driver_group_shift"] = driver_group_shift


    car_group_id = find_car_group(id,date)
    if driver_group_id:
        car_group_shift = object_shift(date,car_group_id,CarGroup)
        if car_group_shift:
            result["car_group_shift"] = car_group_shift



    return result
