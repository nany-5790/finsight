from django.contrib import admin
from .models import Account, Transaction


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ['name', 'tenant', 'owner',
                    'balance', 'currency', 'account_type']
    list_filter = ['account_type', 'currency']
    search_fields = ['name']


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ['account', 'amount',
                    'transaction_type', 'status', 'created_at']
    list_filter = ['status', 'transaction_type']
