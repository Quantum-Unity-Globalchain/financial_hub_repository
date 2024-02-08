import requests

def __init__(self, client_id, client_secret, **kwargs):
    self.client_id = client_id
    self.client_secret = client_secret
    self.base_url = kwargs.get('base_url', 'https://api.saltedge.com/v5')
    self.api_version = kwargs.get('api_version', '5.0')
    self.api_url = f'{self.base_url}/api/v{self.api_version}'
    self.api_headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'App-id': self.client_id,
        'Secret': self.client_secret,
    }

def get_providers(self):
    """
    Retrieves the list of providers.
    """
    endpoint = "/providers"
    try:
        return self._make_request(endpoint)
    except requests.exceptions.RequestException as e:
        print('Error fetching providers:', e)
        return None
