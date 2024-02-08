import os
import plaid
from plaid.api import PlaidApi
from plaid.model import *
from plaid.model.products import Products
from plaid.model.country_code import CountryCode
from plaid.model.item_public_token_exchange_request import ItemPublicTokenExchangeRequest
from plaid.model.link_token_create_request import LinkTokenCreateRequest
from plaid.model.link_token_create_request_user import LinkTokenCreateRequestUser
from plaid.model.accounts_get_request import AccountsGetRequest
from django.conf import settings

class PlaidWrapper:
    def __init__(self):
        configuration = plaid.Configuration(
            host=plaid.Environment.Development,
            api_key={
                'clientId': os.getenv('PLAID_CLIENT_ID'),
                'secret': os.getenv('PLAID_SECRET'),
            }
        )
        api_client = plaid.ApiClient(configuration)
        self.client = PlaidApi(api_client)

    def exchange_public_token(self, public_token):
        """Exchange a Plaid Link public_token for an API access_token."""
        exchange_request = ItemPublicTokenExchangeRequest(
            public_token=public_token
        )
        response = self.client.item_public_token_exchange(exchange_request)
        return response.to_dict()
    def get_accounts(self, access_token):
        """Retrieve accounts for an item."""
        # Example function calls - these would be replaced with actual usage in your application
        # print(self.create_link_token(user_id=123))
        # print(self.exchange_public_token('public-sandbox-...'))
        # print(self.get_accounts('access-sandbox-...'))

        accounts_get_request = AccountsGetRequest(
            access_token=access_token
        )
        response = self.client.accounts_get(accounts_get_request)
        return response.to_dict()

    def create_link_token(self, user_id):
        """Create a link token to initialize Plaid Link."""
        request = LinkTokenCreateRequest(
            user=LinkTokenCreateRequestUser(
                client_user_id=str(user_id)
            ),
            client_name="Financial Hub Integration",
            products=[Products("transactions")],
            country_codes=[CountryCode('US')],
            language="en"
        )
        response = self.client.link_token_create(request)
        return response.to_dict()

# Example usage
if __name__ == "__main__":
    plaid_wrapper = PlaidWrapper()
    user_id = 'your_user_id_here'
    print(plaid_wrapper.create_link_token(user_id=user_id))
