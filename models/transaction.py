from django.db import models
from .account import Account

class Transaction(models.Model):
    # Define the choices for transaction type
    TRANSACTION_TYPES = (
        ('DEP', 'Deposit'),
        ('WDR', 'Withdrawal'),
        ('TRF', 'Transfer'),
    )

    # Link to the Account model via ForeignKey for transaction origin account
    from_account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='outgoing_transactions')
    # Link to the Account model via ForeignKey for transaction destination account (optional for withdrawals/deposits)
    to_account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='incoming_transactions', null=True, blank=True)
    # Transaction type (Deposit, Withdrawal, Transfer)
    transaction_type = models.CharField(max_length=3, choices=TRANSACTION_TYPES)
    # The amount of the transaction
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    # The currency of the transaction amount
    currency = models.CharField(max_length=3)
    # Optional description for the transaction
    description = models.TextField(null=True, blank=True)
    # Creation date of the transaction record
    created_at = models.DateTimeField(auto_now_add=True)
    # Last updated date of the transaction record
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.transaction_type} - {self.amount} {self.currency}"

