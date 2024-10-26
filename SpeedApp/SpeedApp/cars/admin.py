from django.contrib import admin

from SpeedApp.cars.models import Car


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('type', 'model', 'year', 'price')
