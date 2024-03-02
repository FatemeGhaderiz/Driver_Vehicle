from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from ..serializers import DailyShiftSerializer, WeeklyShiftSerializer, MonthlyShiftSerializer, DriverCarShiftSerializer, DriverCarSerializer
from ..services.shift_services import create_daily_shift, create_weekly_shift, create_monthly_shift
from ..selectors.driver_shift import shift_object
from ..selectors.driver_car import driver_car_shift
from ..selectors.interference import check_daily_shift, check_weekly_shift, check_monthly_shift



from django.db.models import Q
from django.contrib.contenttypes.models import ContentType
import datetime
from ..models import DailyShift


class AddDailyShiftApi(APIView):

    serializer_class = DailyShiftSerializer

    def post(self, request):
        serializer = DailyShiftSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        object_type=serializer.validated_data.get("object_type")
        try:
            if object_type == "appointment":
                if check_daily_shift(
                    start_date=serializer.validated_data.get("date_start"),
                    end_date=serializer.validated_data.get("date_end"),
                    start_time=serializer.validated_data.get("time_start"),
                    end_time=serializer.validated_data.get("time_end"),
                    id=serializer.validated_data.get("object_id")
                ):
                    create_daily_shift(
                        date_start=serializer.validated_data.get("date_start"),
                        date_end=serializer.validated_data.get("date_end"),
                        time_start=serializer.validated_data.get("time_start"),
                        time_end=serializer.validated_data.get("time_end"),
                        object_type=serializer.validated_data.get("object_type"),
                        object_id=serializer.validated_data.get("object_id")
                    )
                else:
                    return  Response({"messege" : "errroooor"},status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            return Response(
                {"detail": "Database Error - " + str(ex)},
                status=status.HTTP_400_BAD_REQUEST,
            )
        return Response({"messege" : "Added"},status=status.HTTP_201_CREATED) 





class AddWeeklyShiftApi(APIView):

    serializer_class = WeeklyShiftSerializer

    def post(self, request):
        serializer = WeeklyShiftSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        object_type=serializer.validated_data.get("object_type")
        try:
            if object_type == "appointment":
            
                if check_weekly_shift(
                    start_date=serializer.validated_data.get("date_start"),
                    end_date=serializer.validated_data.get("date_end"),
                    start_time=serializer.validated_data.get("time_start"),
                    end_time=serializer.validated_data.get("time_end"),
                    id=serializer.validated_data.get("object_id"),
                    days=serializer.validated_data.get("days")
                ):
                    create_weekly_shift(
                        date_start=serializer.validated_data.get("date_start"),
                        date_end=serializer.validated_data.get("date_end"),
                        time_start=serializer.validated_data.get("time_start"),
                        time_end=serializer.validated_data.get("time_end"),
                        object_type=serializer.validated_data.get("object_type"),
                        object_id=serializer.validated_data.get("object_id"),
                        days=serializer.validated_data.get("days")
                    )
                else:
                    return Response({"messege" : "errroooor"},status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            return Response(
                {"detail": "Database Error - " + str(ex)},
                status=status.HTTP_400_BAD_REQUEST,
            )
        return Response({"messege" : "Added"},status=status.HTTP_201_CREATED) 




class AddMonthlyShiftApi(APIView):

    serializer_class = MonthlyShiftSerializer

    def post(self, request):
        serializer = MonthlyShiftSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        object_type=serializer.validated_data.get("object_type")
        try:
            if object_type == "appointment":
            
                if check_monthly_shift(
                    start_date=serializer.validated_data.get("date_start"),
                    end_date=serializer.validated_data.get("date_end"),
                    start_time=serializer.validated_data.get("time_start"),
                    end_time=serializer.validated_data.get("time_end"),
                    id=serializer.validated_data.get("object_id"),
                    days=serializer.validated_data.get("days")
                ):
                    create_monthly_shift(
                        date_start=serializer.validated_data.get("date_start"),
                        date_end=serializer.validated_data.get("date_end"),
                        time_start=serializer.validated_data.get("time_start"),
                        time_end=serializer.validated_data.get("time_end"),
                        object_type=serializer.validated_data.get("object_type"),
                        object_id=serializer.validated_data.get("object_id"),
                        days=serializer.validated_data.get("days")
                    )
                else:
                    return Response({"messege" : "errroooor"},status=status.HTTP_400_BAD_REQUEST)     
        except Exception as ex:
            return Response(
                {"detail": "Database Error - " + str(ex)},
                status=status.HTTP_400_BAD_REQUEST,
            )
        return Response({"messege" : "Added"},status=status.HTTP_201_CREATED) 
    









class ShiftApi(APIView):

    serializer_class = DriverCarShiftSerializer

    def post(self, request):
        serializer = DriverCarShiftSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)


        o = 'driver'
        # object_type = ContentType.objects.get(model=o)
        # object = object_type.get_object_for_this_type(id=id)
        # filtered_shifts = DailyShift.objects.filter(
        # Q(date_start__lte=date) & Q(date_end__gte=date) & Q(content_object=object)
    
        try:
            shift = shift_object(
                date=serializer.validated_data.get("date"),
                id=serializer.validated_data.get("object_id"),
                
            )
        except Exception as ex:
            return Response(
                {"detail": "Database Error - " + str(ex)},
                status=status.HTTP_400_BAD_REQUEST,
            )
        return Response(shift,status=status.HTTP_201_CREATED)     
    




class CarDriverApi(APIView):

    serializer_class = DriverCarSerializer

    def post(self, request):
        serializer = DriverCarSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)


        o = 'driver'
        # object_type = ContentType.objects.get(model=o)
        # object = object_type.get_object_for_this_type(id=id)
        # filtered_shifts = DailyShift.objects.filter(
        # Q(date_start__lte=date) & Q(date_end__gte=date) & Q(content_object=object)
    
        try:
            shift = driver_car_shift(
                date=serializer.validated_data.get("date"),
                id=serializer.validated_data.get("object_id"),
                time=serializer.validated_data.get("time"),
                
            )
        except Exception as ex:
            return Response(
                {"detail": "Database Error - " + str(ex)},
                status=status.HTTP_400_BAD_REQUEST,
            )
        return Response(shift,status=status.HTTP_201_CREATED)         