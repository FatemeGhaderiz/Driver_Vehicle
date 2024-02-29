from django.urls import path

from .apis.driver_api import AddDriverApi, AddCarApi, AddDriverGroupeApi, AddCarGroupeApi, CarsGroupeApi, DriversGroupeApi, AppointmentApi

urlpatterns = [
    path("add-driver/", AddDriverApi.as_view(), name="add-driver"),
    path("add-car/", AddCarApi.as_view(), name="add-car"),
    path("add-driver-groupe/", AddDriverGroupeApi.as_view(), name="add-driver-groupe"),
    path("add-car-groupe/", AddCarGroupeApi.as_view(), name="add-car-groupe"),
    path("driver-groupe/", DriversGroupeApi.as_view(), name="driver-groupe"),
    path("car-groupe/", CarsGroupeApi.as_view(), name="car-groupe"),
     path("appointment/", AppointmentApi.as_view(), name="appointment"),
]