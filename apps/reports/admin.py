from django.contrib import admin
from .models import FinancialReport

# Register your models here.


@admin.register(FinancialReport)
class FinancialReportAdmin(admin.ModelAdmin):
    list_display = ['report_type', 'tenant', 'date_from', 'date_to', 'status']
    list_filter = ['report_type', 'status']
