from django.db.models import Q
import datetime
from driver_vehicle_app.models import Appointment


def check_monthly_weekly_days(month_days, week_days, start_date , end_date):
     current_date = start_date
     while current_date <= end_date:
        if current_date.day in month_days:
            if current_date.weekday() in week_days:
                return False
        current_date += datetime.timedelta(days=1)
     return True    




def check_weekly_monthly_days( week_days, month_days, start_date , end_date):
     current_date = start_date
     while current_date <= end_date:
        if current_date.weekday() in week_days:
            if str(current_date.day) in month_days:
                return False
        current_date += datetime.timedelta(days=1)
     return True  


# //////////////////////////////////////////////////////////////////////

def check_driver_car_daily_daily_shift(id, start_date, end_date, start_time, end_time):
    appointment = Appointment.objects.get(id = id)

    if appointment.daily_shift.filter(Q((Q(date_start__lte=start_date) & Q(date_end__gte=start_date)) 
                                      | Q(Q(date_start__lte=end_date) & Q(date_end__gte=end_date))
                                      | Q(Q(date_start__gte=start_date) & Q(date_end__lte=end_date)))
                                      & Q(Q(Q(time_start__lte=start_time) & Q(time_end__gte=start_time)) 
                                      | Q(Q(time_start__lte=end_time) & Q(time_end__gte=end_time))
                                      | Q(Q(time_start__gte=start_time) & Q(time_end__lte=end_time)))).exists():
    
        return False
    return True    



def check_driver_car_daily_weekly_shift(id, start_date, end_date, start_time, end_time):
    appointment = Appointment.objects.get(id = id)

    if appointment.weekly_shift.filter(Q((Q(date_start__lte=start_date) & Q(date_end__gte=start_date)) 
                                      | Q(Q(date_start__lte=end_date) & Q(date_end__gte=end_date))
                                      | Q(Q(date_start__gte=start_date) & Q(date_end__lte=end_date)))
                                      & Q(Q(Q(time_start__lte=start_time) & Q(time_end__gte=start_time)) 
                                      | Q(Q(time_start__lte=end_time) & Q(time_end__gte=end_time))
                                      | Q(Q(time_start__gte=start_time) & Q(time_end__lte=end_time)))).exists():
    
        return False
    return True    



def check_driver_car_daily_monthly_shift(id, start_date, end_date, start_time, end_time):
    appointment = Appointment.objects.get(id = id)

    if appointment.monthly_shift.filter(Q((Q(date_start__lte=start_date) & Q(date_end__gte=start_date)) 
                                      | Q(Q(date_start__lte=end_date) & Q(date_end__gte=end_date))
                                      | Q(Q(date_start__gte=start_date) & Q(date_end__lte=end_date)))
                                      & Q(Q(Q(time_start__lte=start_time) & Q(time_end__gte=start_time)) 
                                      | Q(Q(time_start__lte=end_time) & Q(time_end__gte=end_time))
                                      | Q(Q(time_start__gte=start_time) & Q(time_end__lte=end_time)))).exists():
    
        return False
    return True    



def check_daily_shift(id, start_date, end_date, start_time, end_time):
    if (check_driver_car_daily_daily_shift(id, start_date, end_date, start_time, end_time) and 
       check_driver_car_daily_weekly_shift(id, start_date, end_date, start_time, end_time) and
       check_driver_car_daily_monthly_shift(id, start_date, end_date, start_time, end_time)) :
        return True
    return False
        



# //////////////////////////////////////////////


def check_driver_car_weekly_daily_shift(id, start_date, end_date, start_time, end_time):
    appointment = Appointment.objects.get(id = id)

    if appointment.daily_shift.filter(Q((Q(date_start__lte=start_date) & Q(date_end__gte=start_date)) 
                                      | Q(Q(date_start__lte=end_date) & Q(date_end__gte=end_date))
                                      | Q(Q(date_start__gte=start_date) & Q(date_end__lte=end_date)))
                                      & Q(Q(Q(time_start__lte=start_time) & Q(time_end__gte=start_time)) 
                                      | Q(Q(time_start__lte=end_time) & Q(time_end__gte=end_time))
                                      | Q(Q(time_start__gte=start_time) & Q(time_end__lte=end_time)))).exists():
    
        return False
    return True    





def check_driver_car_weekly_weekly_shift(id, start_date, end_date, start_time, end_time, days):
    appointment = Appointment.objects.get(id = id)

    if appointment.weekly_shift.filter(Q((Q(date_start__lte=start_date) & Q(date_end__gte=start_date)) 
                                      | Q(Q(date_start__lte=end_date) & Q(date_end__gte=end_date))
                                      | Q(Q(date_start__gte=start_date) & Q(date_end__lte=end_date)))
                                      & Q(Q(Q(time_start__lte=start_time) & Q(time_end__gte=start_time)) 
                                      | Q(Q(time_start__lte=end_time) & Q(time_end__gte=end_time))
                                      | Q(Q(time_start__gte=start_time) & Q(time_end__lte=end_time)))).exists():
        
        shift = appointment.weekly_shift.filter(Q((Q(date_start__lte=start_date) & Q(date_end__gte=start_date)) 
                                      | Q(Q(date_start__lte=end_date) & Q(date_end__gte=end_date))
                                      | Q(Q(date_start__gte=start_date) & Q(date_end__lte=end_date)))
                                      & Q(Q(Q(time_start__lte=start_time) & Q(time_end__gte=start_time)) 
                                      | Q(Q(time_start__lte=end_time) & Q(time_end__gte=end_time))
                                      | Q(Q(time_start__gte=start_time) & Q(time_end__lte=end_time))))
        
        for obj in shift:
            li = list(obj.days.split(","))
            for item in days:
                for i in li:
                    if str(item)==i:
                        return False
       
    return True   





def check_driver_car_weekly_monthly_shift(id, start_date, end_date, start_time, end_time, weekdays):
    appointment = Appointment.objects.get(id = id)

    if appointment.monthly_shift.filter(Q((Q(date_start__lte=start_date) & Q(date_end__gte=start_date)) 
                                      | Q(Q(date_start__lte=end_date) & Q(date_end__gte=end_date))
                                      | Q(Q(date_start__gte=start_date) & Q(date_end__lte=end_date)))
                                      & Q(Q(Q(time_start__lte=start_time) & Q(time_end__gte=start_time)) 
                                      | Q(Q(time_start__lte=end_time) & Q(time_end__gte=end_time))
                                      | Q(Q(time_start__gte=start_time) & Q(time_end__lte=end_time)))).exists():
    
        shift = appointment.monthly_shift.filter(Q((Q(date_start__lte=start_date) & Q(date_end__gte=start_date)) 
                                      | Q(Q(date_start__lte=end_date) & Q(date_end__gte=end_date))
                                      | Q(Q(date_start__gte=start_date) & Q(date_end__lte=end_date)))
                                      & Q(Q(Q(time_start__lte=start_time) & Q(time_end__gte=start_time)) 
                                      | Q(Q(time_start__lte=end_time) & Q(time_end__gte=end_time))
                                      | Q(Q(time_start__gte=start_time) & Q(time_end__lte=end_time))))
        
        for obj in shift:
            li = list(obj.days.split(","))
            if not(check_weekly_monthly_days(weekdays,li,start_date,end_date)):
                print(obj)
                print(check_weekly_monthly_days(weekdays,li,start_date,end_date))
                return False

       
    return True   


def check_weekly_shift(id, start_date, end_date, start_time, end_time, days):
    if (check_driver_car_weekly_daily_shift(id, start_date, end_date, start_time, end_time) and 
       check_driver_car_weekly_weekly_shift(id, start_date, end_date, start_time, end_time, days) and
       check_driver_car_weekly_monthly_shift(id, start_date, end_date, start_time, end_time, days)) :
        return True
    return False


# //////////////////////////////////////////////


def check_driver_car_monthly_daily_shift(id, start_date, end_date, start_time, end_time):
    appointment = Appointment.objects.get(id = id)

    if appointment.daily_shift.filter(Q((Q(date_start__lte=start_date) & Q(date_end__gte=start_date)) 
                                      | Q(Q(date_start__lte=end_date) & Q(date_end__gte=end_date))
                                      | Q(Q(date_start__gte=start_date) & Q(date_end__lte=end_date)))
                                      & Q(Q(Q(time_start__lte=start_time) & Q(time_end__gte=start_time)) 
                                      | Q(Q(time_start__lte=end_time) & Q(time_end__gte=end_time))
                                      | Q(Q(time_start__gte=start_time) & Q(time_end__lte=end_time)))).exists():
    
        return False
    return True    




def check_driver_car_monthly_weekly_shift(id, start_date, end_date, start_time, end_time, month_days):
    appointment = Appointment.objects.get(id = id)

    if appointment.weekly_shift.filter(Q((Q(date_start__lte=start_date) & Q(date_end__gte=start_date)) 
                                      | Q(Q(date_start__lte=end_date) & Q(date_end__gte=end_date))
                                      | Q(Q(date_start__gte=start_date) & Q(date_end__lte=end_date)))
                                      & Q(Q(Q(time_start__lte=start_time) & Q(time_end__gte=start_time)) 
                                      | Q(Q(time_start__lte=end_time) & Q(time_end__gte=end_time))
                                      | Q(Q(time_start__gte=start_time) & Q(time_end__lte=end_time)))).exists():
    
        shift = appointment.weekly_shift.filter(Q((Q(date_start__lte=start_date) & Q(date_end__gte=start_date)) 
                                      | Q(Q(date_start__lte=end_date) & Q(date_end__gte=end_date))
                                      | Q(Q(date_start__gte=start_date) & Q(date_end__lte=end_date)))
                                      & Q(Q(Q(time_start__lte=start_time) & Q(time_end__gte=start_time)) 
                                      | Q(Q(time_start__lte=end_time) & Q(time_end__gte=end_time))
                                      | Q(Q(time_start__gte=start_time) & Q(time_end__lte=end_time))))
        
        for obj in shift:
            li = list(obj.days.split(","))
            if not(check_monthly_weekly_days(month_days,li,start_date,end_date)):
                return False

       
    return True   
 





def check_driver_car_monthly_monthly_shift(id, start_date, end_date, start_time, end_time, days):
    appointment = Appointment.objects.get(id = id)

    if appointment.monthly_shift.filter(Q((Q(date_start__lte=start_date) & Q(date_end__gte=start_date)) 
                                      | Q(Q(date_start__lte=end_date) & Q(date_end__gte=end_date))
                                      | Q(Q(date_start__gte=start_date) & Q(date_end__lte=end_date)))
                                      & Q(Q(Q(time_start__lte=start_time) & Q(time_end__gte=start_time)) 
                                      | Q(Q(time_start__lte=end_time) & Q(time_end__gte=end_time))
                                      | Q(Q(time_start__gte=start_time) & Q(time_end__lte=end_time)))).exists():
        
        shift = appointment.monthly_shift.filter(Q((Q(date_start__lte=start_date) & Q(date_end__gte=start_date)) 
                                      | Q(Q(date_start__lte=end_date) & Q(date_end__gte=end_date))
                                      | Q(Q(date_start__gte=start_date) & Q(date_end__lte=end_date)))
                                      & Q(Q(Q(time_start__lte=start_time) & Q(time_end__gte=start_time)) 
                                      | Q(Q(time_start__lte=end_time) & Q(time_end__gte=end_time))
                                      | Q(Q(time_start__gte=start_time) & Q(time_end__lte=end_time))))
        
        for obj in shift:
            li = list(obj.days.split(","))

            for item in days:
                for i in li:
                    if str(item)==i:
                        return False
       
    return True   



def check_monthly_shift(id, start_date, end_date, start_time, end_time, days):
    if (check_driver_car_monthly_daily_shift(id, start_date, end_date, start_time, end_time) and 
       check_driver_car_monthly_weekly_shift(id, start_date, end_date, start_time, end_time, days) and
       check_driver_car_monthly_monthly_shift(id, start_date, end_date, start_time, end_time, days)) :
        return True
    return False

