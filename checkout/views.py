from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


# Create your views here.
def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51QPoO2DNWbx4VwcZCs7HxR9Eu7ctdZYoMvQ5J1OaJJhfOnAs1CF2Oise9QXo2IJyny09ln0n1XuKZPTlEMMTqAZz00iF50F1YX',
        'client_secret': ' test client secret',
    }

    return render(request, template, context)