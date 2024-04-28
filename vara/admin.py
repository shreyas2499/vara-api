from django.contrib import admin

from .models import User, MonthlyConsumption

admin.site.register(User)
admin.site.register(MonthlyConsumption)