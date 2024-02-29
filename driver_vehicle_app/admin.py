from django.contrib import admin
from .models import Driver, Car, DriverGroup, CarGroup, DriversGroup ,CarsGroup, Appointment
# Register your models here.
admin.site.register(Driver)
admin.site.register(Car)
admin.site.register(DriverGroup)
admin.site.register(CarGroup)
admin.site.register(DriversGroup)
admin.site.register(CarsGroup)
admin.site.register(Appointment)