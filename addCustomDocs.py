def add_documentation_entry_to_system(name, docs_url, prefix):
    # Your code to add the entry to your documentation system goes here
    pass

documentation_entries = [
    {"Entrypoint_URL": "https://plaid.com/docs/", "Prefix": "https://plaid.com/docs/", "Name": "Plaid"},
    {"Entrypoint_URL": "https://stripe.com/docs", "Prefix": "https://stripe.com/docs", "Name": "Stripe"},
    {"Entrypoint_URL": "https://docs.finicity.com/", "Prefix": "https://docs.finicity.com/", "Name": "Finicity"},
    {"Entrypoint_URL": "https://developer.yodlee.com/Yodlee_API/", "Prefix": "https://developer.yodlee.com/Yodlee_API/", "Name": "Yodlee"},
    {"Entrypoint_URL": "https://docs.truelayer.com/", "Prefix": "https://docs.truelayer.com/", "Name": "TrueLayer"},
    {"Entrypoint_URL": "https://docs.mx.com/", "Prefix": "https://docs.mx.com/", "Name": "MX Technologies"},
    {"Entrypoint_URL": "https://developers.dwolla.com/", "Prefix": "https://developers.dwolla.com/", "Name": "Dwolla"},
    {"Entrypoint_URL": "https://developer.currencycloud.com/documentation/", "Prefix": "https://developer.currencycloud.com/documentation/", "Name": "Currencycloud"},
    {"Entrypoint_URL": "https://www.hydrogenplatform.com/docs", "Prefix": "https://www.hydrogenplatform.com/docs", "Name": "Hydrogen"},
    {"Entrypoint_URL": "https://www.marqeta.com/api/docs/V3/", "Prefix": "https://www.marqeta.com/api/docs/V3/", "Name": "Marqeta"},
    {"Entrypoint_URL": "https://docs.fidor.com/", "Prefix": "https://docs.fidor.com/", "Name": "Fidor"},
    {"Entrypoint_URL": "https://openbankproject.com/documentation/", "Prefix": "https://openbankproject.com/documentation/", "Name": "Open Bank Project"},
]

for entry in documentation_entries:
    add_documentation_entry_to_system(entry["Name"], entry["Entrypoint_URL"], entry["Prefix"])
