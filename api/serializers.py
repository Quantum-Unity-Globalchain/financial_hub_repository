from rest_framework import serializers
from django.contrib.auth.models import User
from ..models.account import Account
from ..models.transaction import Transaction
from ..models.user_profile import UserProfile

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

class AccountSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Account
        fields = ('id', 'user', 'account_id', 'account_type', 'balance')

class TransactionSerializer(serializers.ModelSerializer):
    account = AccountSerializer(read_only=True)

    class Meta:
        model = Transaction
        fields = ('id', 'account', 'transaction_type', 'amount', 'date', 'description')

class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    accounts = AccountSerializer(many=True, read_only=True)

    class Meta:
        model = UserProfile
        fields = ('id', 'user', 'full_name', 'date_of_birth', 'accounts')
