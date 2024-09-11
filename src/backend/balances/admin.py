from django.contrib import admin

from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models import *

# Register your models here.


class ElectricityBalanceLogResource(resources.ModelResource):

    class Meta:
        model = ElectrictyBalanceLog


@admin.register(ElectricityBalance)
class ElectricityBalanceModelAdmin(admin.ModelAdmin):
    list_display = ['meter_no', 'balance', 'created_at', 'updated_at']

@admin.register(ElectrictyBalanceLog)
class ElectricityBalanceLogModelAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['meter_no', 'voltage_usage', 'current_usage', 'apparent_power', 'timestamp']
    list_filter = ['meter_no', 'timestamp']
    resource_classes = [ElectricityBalanceLogResource]

admin.site.register(Token)
