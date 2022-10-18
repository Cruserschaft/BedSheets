from django.shortcuts import render, redirect
from order.models import *
from cart.cart import *
from product.models import *
import ast


def manager_start(request):
    title = "Всі"
    person = Order.objects.all()
    for item in person:
        item.order = CartWithDict(ast.literal_eval(item.order))

    return render(request, 'manager.html',
                  context={
                      'person': person,
                      'title': title,
                  })


def manager_sorted(request, sort):
    person = Order.objects.filter(status=sort)
    if not person:
        return redirect('manager_start')

    title = ""
    for item in Order.ORDER_CHOICES:
        if item[0] == sort:
            title = item[1]

    for item in person:
        item.order = Cart(ast.literal_eval(item.order))

    return render(request, 'manager.html',
                  context={
                      'person': person,
                      'title': title
                  })


def manager_order(request, order_num):
    person = Order.objects.filter(pk=order_num).first()
    cart = CartWithDict(ast.literal_eval(person.order))

    if not person:
        return redirect('manager_start')

    return render(request, 'manager_order.html',
                  context={
                      'person': person,
                      'cart': cart,
                  })
