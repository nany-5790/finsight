from django.contrib import admin
from .models import AuditLog

# Register your models here.


@admin.register(AuditLog)
class AuditLogAdmin(admin.ModelAdmin):
    list_display = ('user', 'action', 'model_name', 'object_id', 'created_at')
    search_fields = ('user__username', 'action')
    list_filter = ('action', 'model_name')
