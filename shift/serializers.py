from rest_framework import serializers


class DailyShiftSerializer(serializers.Serializer):
    date_start = serializers.DateField()
    date_end = serializers.DateField()
    time_start = serializers.TimeField()
    time_end = serializers.TimeField()
    object_type = serializers.CharField(max_length = 255)
    object_id = serializers.IntegerField()



class WeeklyShiftSerializer(serializers.Serializer):
    date_start = serializers.DateField()
    date_end = serializers.DateField()
    time_start = serializers.TimeField()
    time_end = serializers.TimeField()
    object_type = serializers.CharField(max_length = 255)
    object_id = serializers.IntegerField()
    days = serializers.ListField(child = serializers.IntegerField(min_value = 0, max_value = 6))



class MonthlyShiftSerializer(serializers.Serializer):
    date_start = serializers.DateField()
    date_end = serializers.DateField()
    time_start = serializers.TimeField()
    time_end = serializers.TimeField()
    object_type = serializers.CharField(max_length = 255)
    object_id = serializers.IntegerField()
    days = serializers.ListField(child = serializers.IntegerField(min_value = 1, max_value = 31))





class DriverCarShiftSerializer(serializers.Serializer):
    date = serializers.DateField()
    object_id = serializers.IntegerField()
        



class DriverCarSerializer(serializers.Serializer):
    date = serializers.DateField()
    object_id = serializers.IntegerField()
    time = serializers.TimeField()
                