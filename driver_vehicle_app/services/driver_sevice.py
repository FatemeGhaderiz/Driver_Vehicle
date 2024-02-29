import datetime

from ..models import Driver, Car, DriverGroup, CarGroup, DriversGroup, CarsGroup, Appointment


def create_driver(*, code: str, username: str):

    driver = Driver.objects.create(
        username=username,
        code=code
    )
    return driver



def create_car(*, model: str, license_plate: str):

    driver = Car.objects.create(
        model=model,
        license_plate=license_plate,

    )
    return driver



def create_driver_groupe(*, name: str):

    driver = DriverGroup.objects.create(
        name=name
    )
    return driver



def create_car_groupe(*, name: str):

    driver = CarGroup.objects.create(
        name=name
    )
    return driver



def drivers_groupe(*, driver_code: str, groupe: str):

    driver = Driver.objects.get(code = driver_code)
    groupe_ = DriverGroup.objects.get(name = groupe)
    driver_groupe = DriversGroup.objects.create(
        driver=driver,
        groupe=groupe_
    )
    return driver_groupe



def cars_groupe(*, groupe: str, license_plate: str):
    car = Car.objects.get(license_plate = license_plate)
    groupe_ = CarGroup.objects.get(name = groupe)
    driver = CarsGroup.objects.create(
        car=car,
        groupe=groupe_
    )
    return driver




def appointment(*,  driver_code: str, license_plate: str ,  date_start: datetime.date,  date_end: datetime.date):
    car = Car.objects.get(license_plate = license_plate)
    driver = Driver.objects.get(code = driver_code)
    driver = Appointment.objects.create(
        car=car,
        driver=driver,
        date_start=date_start,
        date_end=date_end
    )
    return driver