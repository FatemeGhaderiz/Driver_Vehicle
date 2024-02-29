from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType



class DailyShift(models.Model):
    date_start = models.DateField()
    date_end = models.DateField()
    time_start = models.TimeField()
    time_end = models.TimeField()

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()





class WeeklyShift(models.Model):
    date_start = models.DateField()
    date_end = models.DateField()
    time_start = models.TimeField()
    time_end = models.TimeField()
    days = models.CharField(max_length = 13)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()    




class MonthlyShift(models.Model):
    date_start = models.DateField()
    date_end = models.DateField()
    time_start = models.TimeField()
    time_end = models.TimeField()
    days = models.CharField(max_length = 61)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()    

