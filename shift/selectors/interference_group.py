
from django.db.models import Q

from driver_vehicle_app.models import DriverGroup, DriversGroup, Driver, Appointment
from .interference import check_driver_car_daily_daily_shift, check_driver_car_daily_weekly_shift, check_driver_car_daily_monthly_shift 
from .interference import check_driver_car_weekly_daily_shift, check_driver_car_weekly_weekly_shift, check_driver_car_weekly_monthly_shift 
from .interference import check_driver_car_monthly_daily_shift, check_driver_car_monthly_weekly_shift, check_driver_car_monthly_monthly_shift 


def find_drivers_of_group(id):
    drivers_id = []
    group = DriverGroup.objects.get(id=id)

    driver_group = DriversGroup.objects.filter(groupe = group)
    for item in driver_group :
        drivers_id.append(item.driver.id)

    return drivers_id    



def find_drivers_appoinment(id,start_date,end_date):
    driver = Driver.objects.get(id=id)
    object = Appointment.objects.get(((Q(date_start__lte=start_date) & Q(date_end__gte=start_date)) 
                                      | Q(Q(date_start__lte=end_date) & Q(date_end__gte=end_date))
                                      | Q(Q(date_start__gte=start_date) & Q(date_end__lte=end_date)))) 
    return object.id    





def check_driver_groupe_daily_shift(id, start_date, end_date, start_time, end_time):

    drivers_id = find_drivers_of_group(id)

    for driver in drivers_id:
        appointment = find_drivers_appoinment(driver,start_date,end_date)
        if (check_driver_car_daily_daily_shift(appointment,start_date,end_date,start_time,end_time) or
           check_driver_car_daily_weekly_shift(appointment,start_date,end_date,start_time,end_time) or
           check_driver_car_daily_monthly_shift(appointment,start_date,end_date,start_time,end_time)):
            return False

    return True       




def check_driver_groupe_weekly_shift(id, start_date, end_date, start_time, end_time, days):

    drivers_id = find_drivers_of_group(id)

    for driver in drivers_id:
        appointment = find_drivers_appoinment(driver,start_date,end_date)
        if (check_driver_car_weekly_daily_shift(appointment,start_date,end_date,start_time,end_time, days) or
           check_driver_car_weekly_weekly_shift(appointment,start_date,end_date,start_time,end_time, days) or
           check_driver_car_weekly_monthly_shift(appointment,start_date,end_date,start_time,end_time, days)):
            return False

    return True       





def check_driver_groupe_weekly_shift(id, start_date, end_date, start_time, end_time, days):

    drivers_id = find_drivers_of_group(id)

    for driver in drivers_id:
        appointment = find_drivers_appoinment(driver,start_date,end_date)
        if (check_driver_car_monthly_daily_shift(appointment,start_date,end_date,start_time,end_time, days) or
           check_driver_car_monthly_weekly_shift(appointment,start_date,end_date,start_time,end_time, days) or
           check_driver_car_monthly_monthly_shift(appointment,start_date,end_date,start_time,end_time, days)):
            return False

    return True       


# ////////////////////////////////////////////////////////////////

