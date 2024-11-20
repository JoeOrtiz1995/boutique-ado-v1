from django.shortcuts import render

# Create your views here.
def view_bag(request):
    """
    View that returns the contents in a user's bag/cart
    """

    return render(request, 'bag/bag.html')
