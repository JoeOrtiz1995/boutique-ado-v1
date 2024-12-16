from django.http import HttpResponse


class StripeWH_Handler:
    """
    Handle Stripe Webhooks.
    """

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Handle a generic, unknown or unexpected webhook event.
        """
        return HttpResponse(
            content = f'Unhandled Webhook received: {event["type"]}',
            status = 200)

    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment_intent.succeeded Stripe webhook.
        """
        intent = event.data.object
        print(intent)
        return HttpResponse(
            content = f'Webhook received: {event["type"]}',
            status = 200)

    def handle_payment_intent_failed(self, event):
        """
        Handle the payment_intent.payment_failed Stripe webhook.
        """
        return HttpResponse(
            content = f'Payment Failed Webhook received: {event["type"]}',
            status = 200)