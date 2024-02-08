"""
Configuration for HTTPS in Django for the Financial Hub Integration project.
"""

from django.core.exceptions import ImproperlyConfigured

def enforce_https_middleware(get_response):
    """
    Middleware to enforce HTTPS on all requests.
    """
    def middleware(request):
        if not request.is_secure():
            if "HTTP_X_FORWARDED_PROTO" in request.META:
                if request.META["HTTP_X_FORWARDED_PROTO"] != "https":
                    raise ImproperlyConfigured("Insecure request received over HTTP. This application requires HTTPS.")
            else:
                raise ImproperlyConfigured("Insecure request received. This application requires HTTPS.")
        return get_response(request)
    
    return middleware

# Add the enforce_https_middleware to the MIDDLEWARE list in settings.py
# Example:
# MIDDLEWARE = [
#     ...
#     'path.to.security.https_config.enforce_https_middleware',
#     ...
# ]
def add_documentation_entry_to_system(name, docs_url, prefix):
    # Your code to add the entry to your documentation system goes here
    pass

# Define the documentation_entries list
documentation_entries = [
    {"Name": "Entry1", "Entrypoint_URL": "https://example.com/entry1", "Prefix": "entry1"},
    {"Name": "Entry2", "Entrypoint_URL": "https://example.com/entry2", "Prefix": "entry2"},
    # Add more entries as needed
]

# Adjust the loop to pass the correct parameters from each entry
for entry in documentation_entries:
    add_documentation_entry_to_system(entry["Name"], entry["Entrypoint_URL"], entry["Prefix"])