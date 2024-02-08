import requests
from django.conf import settings

class RevolutAPIException(Exception):
    """Custom exception for Revolut API errors"""
    pass

class RevolutWrapper:
    """
    A wrapper class for interacting with the Revolut API.
    """
    def __init__(self):
        self.base_url = "https://api.revolut.com"
        self.api_key = settings.REVOLUT_API_KEY

    def _send_request(self, method, endpoint, data=None):
        """
        Sends a request to the Revolut API.
        """
        url = f"{self.base_url}{endpoint}"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        response = requests.request(method, url, headers=headers, json=data)
        if response.status_code not in range(200, 299):
            raise RevolutAPIException(f"API request failed with status code {response.status_code}: {response.text}")
        return response.json()

    def create_payment(self, request_data):
        """
        Creates a new payment.
        """
        endpoint = "/payments"
        return self._send_request("POST", endpoint, data=request_data)

    def get_account_details(self, account_id):
        """
        Retrieves details for a specific account.
        """
        endpoint = f"/accounts/{account_id}"
        return self._send_request("GET", endpoint)

    def exchange_currency(self, request_data):
        """
        Performs a currency exchange.
        """
        endpoint = "/exchange"
        return self._send_request("POST", endpoint, data=request_data)

# Example usage
if __name__ == "__main__":
    revolut = RevolutWrapper()
    try:
        account_details = revolut.get_account_details("your-account-id")
        print(account_details)
    except RevolutAPIException as e:
        print(f"Error: {e}")
