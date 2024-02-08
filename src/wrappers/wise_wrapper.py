import requests
from django.conf import settings

class WiseWrapper:
    """
    A wrapper class for interacting with the Wise API.
    """
    def __init__(self):
        self.base_url = "https://api.transferwise.com"
        self.api_key = settings.WISE_API_KEY

    def _make_request(self, endpoint, method="GET", data=None):
        """
        Makes a request to the Wise API.
        """
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        url = f"{self.base_url}{endpoint}"

        if method == "GET":
            response = requests.get(url, headers=headers)
        elif method == "POST":
            response = requests.post(url, headers=headers, json=data)
        else:
            raise ValueError("Unsupported HTTP method")

        if response.status_code not in [200, 201]:
            raise Exception(f"API request failed with status code {response.status_code}: {response.text}")

        return response.json()

    def get_profiles(self):
        """
        Retrieves the user's profiles.
        """
        endpoint = "/v1/profiles"
        return self._make_request(endpoint)

    def create_quote(self, profile_id, source_currency, target_currency, target_amount):
        """
        Creates a quote for a money transfer.
        """
        endpoint = "/v2/quotes"
        data = {
            "profile": profile_id,
            "source": source_currency,
            "target": target_currency,
            "targetAmount": target_amount,
            "rateType": "FIXED"
        }
        return self._make_request(endpoint, method="POST", data=data)

    def create_transfer(self, profile_id, quote_id, recipient_id, details):
        """
        Creates a transfer.
        """
        endpoint = "/v1/transfers"
        data = {
            "targetAccount": recipient_id,
            "quote": quote_id,
            "customerTransactionId": f"tx_{profile_id}_{quote_id}",
            "details": details
        }
        return self._make_request(endpoint, method="POST", data=data)

    def fund_transfer(self, transfer_id):
        """
        Funds a transfer. This is a simplified example and in a real scenario,
        you would need to handle the funding process according to the Wise API documentation.
        """
        endpoint = f"/v3/profiles/{transfer_id}/payments"
        # This is a placeholder. In a real implementation, you would need to follow the
        # Wise API's instructions for funding a transfer, which might involve redirecting
        # the user to complete the payment or handling bank details.
        print("This method is a placeholder and should be implemented according to the Wise API documentation.")
    def add_documentation_entry_to_system(name, docs_url, prefix):
        """
        Adds a documentation entry to the system.
        """
        # Your code to add the entry to your documentation system goes here
        pass

    documentation_entries = [
        {"Entrypoint_URL": "/v1/profiles", "Prefix": "/v1", "Name": "Profiles"},
        {"Entrypoint_URL": "/v2/quotes", "Prefix": "/v2", "Name": "Quotes"},
        {"Entrypoint_URL": "/v1/transfers", "Prefix": "/v1", "Name": "Transfers"},
        {"Entrypoint_URL": "/v3/profiles/{transfer_id}/payments", "Prefix": "/v3", "Name": "Payments"}
    ]

    for entry in documentation_entries:
        add_documentation_entry_to_system(entry["Name"], entry["Entrypoint_URL"], entry["Prefix"])
