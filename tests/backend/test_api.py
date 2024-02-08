import json
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from models.account import Account
from models.transaction import Transaction
from models.user_profile import UserProfile

# Define the documentation entries
documentation_entries = [
    {"Name": "Entry1", "Entrypoint_URL": "https://example.com/entry1", "Prefix": "entry1"},
    {"Name": "Entry2", "Entrypoint_URL": "https://example.com/entry2", "Prefix": "entry2"},
    # Add more entries as needed
]

def add_documentation_entry_to_system(name, entrypoint_url, prefix):
    # Implementation to add the documentation entry to the system
    pass

for entry in documentation_entries:
    add_documentation_entry_to_system(entry["Name"], entry["Entrypoint_URL"], entry["Prefix"])

class AccountAPITests(APITestCase):
    def setUp(self):
        # Create a user
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='testpassword')
        self.client.login(username='testuser', password='testpassword')
        
        # Create a UserProfile for the user
        self.user_profile = UserProfile.objects.create(user=self.user, full_name='Test User', phone_number='1234567890')
        
        # Create an Account for the user
        self.account = Account.objects.create(user=self.user, account_id='12345', account_type='savings', balance=1000)
        
        # Create a Transaction for the account
        self.transaction = Transaction.objects.create(account=self.account, transaction_type='deposit', amount=100, description='Initial deposit')

    def test_get_accounts(self):
        url = reverse('account-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['user']['username'], 'testuser')

    def test_create_transaction(self):
        url = reverse('transaction-list')
        data = {'account': self.account.id, 'transaction_type': 'withdraw', 'amount': 50, 'description': 'Test withdraw'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Transaction.objects.count(), 2)
        self.assertEqual(Transaction.objects.latest('id').amount, 50)

    def test_user_profile(self):
        url = reverse('userprofile-detail', kwargs={'pk': self.user_profile.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['full_name'], 'Test User')

    def test_unauthorized_access(self):
        self.client.logout()
        url = reverse('account-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
