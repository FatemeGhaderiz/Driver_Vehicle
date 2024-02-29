import datetime
from django.contrib.contenttypes.models import ContentType

from ..models import DailyShift, WeeklyShift, MonthlyShift


def create_daily_shift(*, date_start: datetime.date, date_end: datetime.date, time_start: datetime.time, time_end: datetime.time, object_type: str, object_id: int):
    object_type = ContentType.objects.get(model=object_type)
    object = object_type.get_object_for_this_type(id=object_id)
    shift = DailyShift.objects.create(
        date_start=date_start,
        date_end=date_end,
        time_start=time_start,
        time_end=time_end,
        content_object=object
    )
    return shift




def create_weekly_shift(*, date_start: datetime.date, date_end: datetime.date, time_start: datetime.time
                        ,time_end: datetime.time, object_type: str, object_id: int , days: list):
    
    days_ = ",".join(str(element) for element in days)
    object_type = ContentType.objects.get(model=object_type)
    object = object_type.get_object_for_this_type(id=object_id)
    shift = WeeklyShift.objects.create(
        date_start=date_start,
        date_end=date_end,
        time_start=time_start,
        time_end=time_end,
        content_object=object,
        days = days_
    )
    return shift



def create_monthly_shift(*, date_start: datetime.date, date_end: datetime.date, time_start: datetime.time
                        ,time_end: datetime.time, object_type: str, object_id: int , days: list):
    
    days_ = ",".join(str(element) for element in days)
    object_type = ContentType.objects.get(model=object_type)
    object = object_type.get_object_for_this_type(id=object_id)
    shift = MonthlyShift.objects.create(
        date_start=date_start,
        date_end=date_end,
        time_start=time_start,
        time_end=time_end,
        content_object=object,
        days = days_
    )
    return shift