from django.db import models
from django.contrib.auth.models import User

class Account(models.Model):
    # Define the choices for account type
    ACCOUNT_TYPES = (
        ('SAV', 'Savings'),
        ('CHK', 'Checking'),
        ('INV', 'Investment'),
    )

    # Link to the Django built-in User model via ForeignKey for account ownership
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='accounts')
    # Account identifier, could be an account number or similar unique identifier
    account_id = models.CharField(max_length=255, unique=True)
    # Account type (Savings, Checking, Investment, etc.)
    account_type = models.CharField(max_length=3, choices=ACCOUNT_TYPES)
    # The current balance of the account
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    # The currency of the account balance
    currency = models.CharField(max_length=3)
    # The name of the financial institution the account belongs to
    institution_name = models.CharField(max_length=255)
    # Creation date of the account record
    created_at = models.DateTimeField(auto_now_add=True)
    # Last updated date of the account record
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username}'s {self.get_account_type_display()} Account - {self.institution_name}"

