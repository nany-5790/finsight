import uuid
from django.db import models

from apps.accounts.models import UserProfile
from apps.core.models import SoftDeleteModel
from apps.tenants.models import Tenant


# Create your models here.

class Account(SoftDeleteModel):
    class ACCOUNT_TYPES(models.TextChoices):
        CHECKING = 'checking', 'Checking'
        SAVINGS = 'savings', 'Savings'
        INVESTMENT = 'investment', 'Investment'

    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=19, decimal_places=4)
    currency = models.CharField(max_length=3, default='USD')
    account_type = models.CharField(max_length=20, choices=ACCOUNT_TYPES)

    def __str__(self):
        return f"{self.name} - {self.balance}"


class Transaction(SoftDeleteModel):
    class STATUSES(models.TextChoices):
        PENDING = 'pending', 'Pending'
        COMPLETED = 'completed', 'Completed'
        FAILED = 'failed', 'Failed'
        CANCELED = 'canceled', 'Canceled'
        PROCESSING = 'processing', 'Processing'

    class TRANSACTION_TYPES(models.TextChoices):
        CREDIT = 'credit', 'Credit'
        DEBIT = 'debit', 'Debit'
        TRANSFER = 'transfer', 'Transfer'

    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=19, decimal_places=4)
    idempotency_key = models.UUIDField(unique=True, default=uuid.uuid4)
    description = models.TextField(blank=True)
    status = models.CharField(
        max_length=20, choices=STATUSES.choices, default='pending')
    reference = models.CharField(max_length=255, blank=True)
    transaction_type = models.CharField(
        max_length=20, choices=TRANSACTION_TYPES.choices)

    def __str__(self):
        return f"{self.amount} {self.status}"
