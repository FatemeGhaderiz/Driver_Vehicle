from rest_framework import serializers
from .models import Driver, Car, DriverGroup, CarGroup


class DriverSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Driver
        fields = ("username", "code")



class CarSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Car
        fields = ("model", "license_plate")



class DriverGroupSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = DriverGroup
        fields = ("name",)



class CarGroupSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = CarGroup
        fields = ("name",)




class DriversGroupSerializer(serializers.Serializer):
   driver_code = serializers.CharField(max_length=10)
   groupe = serializers.CharField(max_length=255)



class CarsGroupSerializer(serializers.Serializer):
   license_plate = serializers.CharField(max_length=20)
   groupe = serializers.CharField(max_length=255)
            


class AppointmentSerializer(serializers.Serializer):
    license_plate = serializers.CharField(max_length=20)
    driver_code = serializers.CharField(max_length=10)
    date_start = serializers.DateField()
    date_end = serializers.DateField()