from django.urls import path, include

app_name = "api"
urlpatterns = [
    path("driver-vehicle/", include(("driver_vehicle_app.urls", "driver-vehicle"))),
    path("shift/", include(("shift.urls", "shift"))),
]
