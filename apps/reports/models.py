from django.db import models
from django.db.models import Sum, Count, Avg
from django.contrib.auth.models import User


from apps.tenants.models import Tenant
from apps.core.models import TimeStampedModel

# Create your models here.


class FinancialReport(TimeStampedModel):
    class ReportType(models.TextChoices):
        DAILY = 'daily', 'Daily'
        WEEKLY = 'weekly', 'Weekly'
        MONTHLY = 'monthly', 'Monthly'
        ANNUAL = 'annual', 'Annual'

    class STATUS(models.TextChoices):
        GENERATED = 'generated', 'Generated'
        PENDING = 'pending', 'Pending'
        FAILED = 'failed', 'Failed'

    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    generated_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True)
    report_type = models.CharField(max_length=50, choices=ReportType.choices)
    date_from = models.DateField()
    date_to = models.DateField()
    total_debits = models.DecimalField(
        max_digits=19, decimal_places=4, default=0)
    total_credits = models.DecimalField(
        max_digits=19, decimal_places=4, default=0)
    net_balance = models.DecimalField(
        max_digits=19, decimal_places=4, default=0)
    status = models.CharField(max_length=20, choices=STATUS.choices)

    def __str__(self):
        return f"{self.report_type} - {self.date_from} / {self.date_to}"

    class Meta:
        ordering = ['-date_from']
        verbose_name = 'Financial Report'
