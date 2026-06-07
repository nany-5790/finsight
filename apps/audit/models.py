from django.db import models
from django.contrib.auth.models import User

from apps.core.models import TimeStampedModel
from apps.tenants.models import Tenant

# Create your models here.


class AuditLog(TimeStampedModel):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    action = models.CharField(max_length=255)
    model_name = models.CharField(max_length=255)
    object_id = models.CharField(max_length=100)
    changes = models.JSONField(null=True)
    ip_address = models.GenericIPAddressField(null=True)

    def save(self, *args, **kwargs):
        if self.pk:
            raise PermissionError("Audit logs are immutable.")
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        raise PermissionError("Audit logs cannot be deleted.")

    def __str__(self):
        return f"{self.created_at} - {self.user} - {self.action}"
