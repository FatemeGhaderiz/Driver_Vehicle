from django.urls import path

from .apis.shift_api import AddDailyShiftApi, AddWeeklyShiftApi, AddMonthlyShiftApi, ShiftApi, CarDriverApi

urlpatterns = [
    path("add-daily-shift/", AddDailyShiftApi.as_view(), name="add-daily-shift"),
    path("add-weekly-shift/", AddWeeklyShiftApi.as_view(), name="add-weekly-shift"),
    path("add-monthly-shift/", AddMonthlyShiftApi.as_view(), name="add-monthly-shift"),
    path("driver-shift/", ShiftApi.as_view(), name="driver-shift"),
    path("driver-car/", CarDriverApi.as_view(), name="driver-car"),
]