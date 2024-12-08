from django.http import HttpResponse


class StripeWH_Handler:
    """
    Handle Stripe Webhooks.
    """

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Handle Stripe Webhooks.
        """
        return HttpResponse(
            content = f'Webhook received: {event["type"]}',
            status = 200)