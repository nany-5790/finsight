from django.contrib import admin
from apps.tenants.models import Tenant


# Register your models here.

@admin.register(Tenant)
class TenantAdmin(admin.ModelAdmin):
    list_display = ('name', 'tax_id', 'plan', 'is_verified', 'is_active')
    search_fields = ('name', 'domain', 'tax_id')
    list_filter = ('plan', 'is_verified')
