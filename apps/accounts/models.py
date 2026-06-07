from django.db import models
from django.contrib.auth.models import User

from apps.tenants.models import Tenant
from apps.core.models import SoftDeleteModel, TimeStampedModel


# Create your models here.

class UserProfile(SoftDeleteModel):
    class Role(models.TextChoices):
        ADMIN = 'admin', 'Admin'
        ACCOUNTANT = 'accountant', 'Accountant'
        AUDITOR = 'auditor', 'Auditor'
        VIEWER = 'viewer', 'Viewer'
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    role = models.CharField(
        max_length=50, choices=Role.choices, default=Role.VIEWER)
    phone = models.CharField(max_length=20, blank=True, null=True)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


class AuditUserAction(TimeStampedModel):
    class Action(models.TextChoices):
        LOGIN = 'login', 'Login'
        LOGOUT = 'logout', 'Logout'
        FAILED_LOGIN = 'failed_login', 'Failed Login'
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    action = models.CharField(max_length=255, choices=Action.choices)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    user_agent = models.TextField(blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.action} at {self.created_at}"
