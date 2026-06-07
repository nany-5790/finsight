from django.contrib import admin
from .models import UserProfile, AuditUserAction


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'tenant', 'role', 'is_verified']
    list_filter = ['role', 'is_verified']
    search_fields = ['user__username']


@admin.register(AuditUserAction)
class AuditUserActionAdmin(admin.ModelAdmin):
    list_display = ['user', 'action', 'ip_address', 'created_at']
    list_filter = ['action']
