from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from ..serializers import DriverSerializer, CarSerializer, DriverGroupSerializer, CarGroupSerializer, DriversGroupSerializer, CarsGroupSerializer, AppointmentSerializer

from ..services.driver_sevice import create_driver, create_car, create_car_groupe, create_driver_groupe, cars_groupe, drivers_groupe, appointment



class AddDriverApi(APIView):

    serializer_class = DriverSerializer

    def post(self, request):
        serializer = DriverSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            query = create_driver(
                username=serializer.validated_data.get("username"),
                code=serializer.validated_data.get("code")
            )
        except Exception as ex:
            return Response(
                {"detail": "Database Error - " + str(ex)},
                status=status.HTTP_400_BAD_REQUEST,
            )
        return Response(DriverSerializer(query, context={"request": request}).data)



class AddCarApi(APIView):

    serializer_class = CarSerializer

    def post(self, request):
        serializer = CarSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            query = create_car(
                model=serializer.validated_data.get("model"),
                license_plate=serializer.validated_data.get("license_plate")
            )
        except Exception as ex:
            return Response(
                {"detail": "Database Error - " + str(ex)},
                status=status.HTTP_400_BAD_REQUEST,
            )
        return Response(CarSerializer(query, context={"request": request}).data)




class AddDriverGroupeApi(APIView):

    serializer_class = DriverGroupSerializer

    def post(self, request):
        serializer = DriverGroupSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            query = create_driver_groupe(
                name=serializer.validated_data.get("name"),
            )
        except Exception as ex:
            return Response(
                {"detail": "Database Error - " + str(ex)},
                status=status.HTTP_400_BAD_REQUEST,
            )
        return Response(DriverGroupSerializer(query, context={"request": request}).data)



class AddCarGroupeApi(APIView):

    serializer_class = CarGroupSerializer

    def post(self, request):
        serializer = CarGroupSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            query = create_car_groupe(
                name=serializer.validated_data.get("name"),
            )
        except Exception as ex:
            return Response(
                {"detail": "Database Error - " + str(ex)},
                status=status.HTTP_400_BAD_REQUEST,
            )
        return Response(CarGroupSerializer(query, context={"request": request}).data)
    



class CarsGroupeApi(APIView):

    serializer_class = CarsGroupSerializer

    def post(self, request):
        serializer = CarsGroupSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            query = cars_groupe(
                license_plate=serializer.validated_data.get("license_plate"),
                groupe=serializer.validated_data.get("groupe")
            )
        except Exception as ex:
            return Response(
                {"detail": "Database Error - " + str(ex)},
                status=status.HTTP_400_BAD_REQUEST,
            )
        return Response({"messege" : "Added"},status=status.HTTP_201_CREATED)    




class DriversGroupeApi(APIView):

    serializer_class = DriversGroupSerializer

    def post(self, request):
        serializer = DriversGroupSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            query = drivers_groupe(
                driver_code=serializer.validated_data.get("driver_code"),
                groupe=serializer.validated_data.get("groupe")
            )
        except Exception as ex:
            return Response(
                {"detail": "Database Error - " + str(ex)},
                status=status.HTTP_400_BAD_REQUEST,
            )
        return Response({"messege" : "Added"},status=status.HTTP_201_CREATED)     
    




class AppointmentApi(APIView):

    serializer_class = AppointmentSerializer

    def post(self, request):
        serializer = AppointmentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            query = appointment(
                driver_code=serializer.validated_data.get("driver_code"),
                license_plate=serializer.validated_data.get("license_plate"),
                date_start=serializer.validated_data.get("date_start"),
                date_end=serializer.validated_data.get("date_end")
            )
        except Exception as ex:
            return Response(
                {"detail": "Database Error - " + str(ex)},
                status=status.HTTP_400_BAD_REQUEST,
            )
        return Response({"messege" : "Added"},status=status.HTTP_201_CREATED)             