from django.test import TestCase
from django.contrib.auth.models import User
from your_project.models.account import Account
from your_project.models.transaction import Transaction

class AccountModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        test_user = User.objects.create_user(username='testuser', password='12345')
        Account.objects.create(user=test_user, account_id='123456789', account_type='SAV', balance=1000.00)

    def test_account_content(self):
        account = Account.objects.get(id=1)
        expected_user = account.user.username
        expected_account_id = account.account_id
        expected_account_type = account.get_account_type_display()
        expected_balance = account.balance
        self.assertEquals(expected_user, 'testuser')
        self.assertEquals(expected_account_id, '123456789')
        self.assertEquals(expected_account_type, 'Savings')
        self.assertEquals(expected_balance, 1000.00)

class TransactionModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        test_user = User.objects.create_user(username='testuser', password='12345')
        test_account = Account.objects.create(user=test_user, account_id='123456789', account_type='SAV', balance=1000.00)
        Transaction.objects.create(account=test_account, transaction_type='DEP', amount=100.00, description="Initial deposit")

    def test_transaction_content(self):
        transaction = Transaction.objects.get(id=1)
        expected_account_id = transaction.account.account_id
        expected_transaction_type = transaction.get_transaction_type_display()
        expected_amount = transaction.amount
        expected_description = transaction.description
        self.assertEquals(expected_account_id, '123456789')
        self.assertEquals(expected_transaction_type, 'Deposit')
        self.assertEquals(expected_amount, 100.00)
        self.assertEquals(expected_description, "Initial deposit")
