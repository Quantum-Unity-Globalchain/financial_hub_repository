import requests
from django.conf import settings

class IntradataWrapper:
    """
    A wrapper class for interacting with the Intradata API.
    """
    def __init__(self):
        self.base_url = "https://api.intradata.com/"
        self.api_key = settings.INTRADATA_API_KEY

    def get_headers(self):
        """
        Returns the headers required for making requests to the Intradata API.
        """
        return {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

    def get_financial_data(self, endpoint, params=None):
        """
        Generic method to fetch financial data from a specific endpoint.
        :param endpoint: The Intradata API endpoint to hit.
        :param params: Optional parameters to include in the request.
        :return: JSON response from the API.
        """
        try:
            response = requests.get(f"{self.base_url}{endpoint}", headers=self.get_headers(), params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as e:
            print(f"HTTPError while fetching data from Intradata: {e}")
        except requests.exceptions.RequestException as e:
            print(f"RequestException while fetching data from Intradata: {e}")
        except Exception as e:
            print(f"Unexpected error while fetching data from Intradata: {e}")

    def get_market_summary(self):
        """
        Fetches the market summary data.
        :return: Market summary data as JSON.
        """
        return self.get_financial_data("market/summary")

    def get_stock_info(self, symbol):
        """
        Fetches stock information for a given symbol.
        :param symbol: The stock symbol to fetch information for.
        :return: Stock information as JSON.
        """
        return self.get_financial_data(f"stock/{symbol}")

# Example usage
# intradata = IntradataWrapper()
# market_summary = intradata.get_market_summary()
# print(market_summary)
# stock_info = intradata.get_stock_info('AAPL')
# print(stock_info)
