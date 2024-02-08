import stripe
from django.conf import settings

class StripeWrapper:
    def __init__(self):
        stripe.api_key = settings.STRIPE_API_KEY

    def create_charge(self, amount, currency, source, description=""):
        """
        Create a charge on Stripe.
        :param amount: Amount to be charged (in cents).
        :param currency: Currency code (e.g., 'usd').
        :param source: Source token (e.g., a token from Stripe Checkout).
        :param description: Optional description of the charge.
        :return: Stripe charge object or None if an error occurs.
        """
        try:
            charge = stripe.Charge.create(
                amount=amount,
                currency=currency,
                source=source,
                description=description
            )
            return charge
        except stripe.error.StripeError as e:
            # Log the error
            print("Stripe Error: {e.user_message}")
            return None

    def create_customer(self, email, source):
        """
        Create a new customer on Stripe.
        :param email: Customer's email address.
        :param source: Source token (e.g., a token from Stripe Checkout).
        :return: Stripe customer object or None if an error occurs.
        """
        try:
            customer = stripe.Customer.create(
                email=email,
                source=source
            )
            return customer
        except stripe.error.StripeError as e:
            # Log the error
            print("Stripe Error: {e.user_message}")
            return None

    def create_subscription(self, customer_id, plan_id):
        """
        Create a subscription for a customer to a plan.
        :param customer_id: The Stripe Customer ID.
        :param plan_id: The Stripe Plan ID to subscribe the customer to.
        :return: Stripe subscription object or None if an error occurs.
        """
        try:
            subscription = stripe.Subscription.create(
                customer=customer_id,
                items=[{'plan': plan_id}],
            )
            return subscription
        except stripe.error.StripeError as e:
            # Log the error
            print("Stripe Error: {e.user_message}")
            return None

# Remember to replace 'your-stripe-api-key' with your actual Stripe secret key
# in your Django settings file (settings.py), under the variable name STRIPE_API_KEY.
