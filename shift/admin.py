from django.contrib import admin

# Register your models here.
from .models import DailyShift, WeeklyShift, MonthlyShift

admin.site.register(DailyShift)
admin.site.register(WeeklyShift)
admin.site.register(MonthlyShift)