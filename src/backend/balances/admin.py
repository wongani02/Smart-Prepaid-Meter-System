from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(ElectricityBalance)
class ElectricityBalanceModelAdmin(admin.ModelAdmin):
    list_display = ['meter_no', 'balance', 'created_at', 'updated_at']

admin.site.register(Token)
admin.site.register(ElectrictyBalanceLog)