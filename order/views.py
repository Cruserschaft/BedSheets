from django.shortcuts import render
from BedSheets.settings import CART_SESSION_ID
from cart.cart import Cart
from .forms import *


def start_order(request):
    err = None
    cart = Cart(request)
    form = OrderForm()

    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            print("Все вірно")
            # request.session.get(CART_SESSION_ID)
            form_update = form.save(commit=True)
            form_update.order = request.session.get(CART_SESSION_ID)

            form_update.save()
            form = OrderForm()
        else:
            err = form.errors.as_data()
            print(err)

    return render(request, 'order.html',
                  context={
                      'cart': cart,
                      'form': form,
                      'error': err,
                  })