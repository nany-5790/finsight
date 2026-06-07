from django.db import models

from apps.core.models import SoftDeleteModel

# Create your models here.

# Tenant model inherits from SoftDeletecModel.


class Tenant(SoftDeleteModel):
    class Plan(models.TextChoices):
        FREE = 'free', 'Free'
        PRO = 'pro', 'Pro'
        ENTERPRISE = 'enterprise', 'Enterprise'
    name = models.CharField(max_length=255)
    domain = models.CharField(max_length=100, unique=True)
    tax_id = models.CharField(max_length=100, unique=True)
    is_verified = models.BooleanField(default=False)
    plan = models.CharField(
        max_length=50, default=Plan.FREE, choices=Plan.choices)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Tenant'
        verbose_name_plural = 'Tenants'
