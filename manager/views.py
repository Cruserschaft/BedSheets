from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from order.models import *
from cart.cart import *
from .forms import *
from product.models import *
import ast





def manager_start(request):
    title = "Всі"

    person = Order.objects.all()

    if request.method == "POST":
        person = Order.objects.filter(person_uuid=request.POST['search'])

    if not person:
        return redirect(request.META.get('HTTP_REFERER'))

    for item in person:
        item.order = CartWithDict(ast.literal_eval(item.order))

    form = OrderSearch()

    paginator = Paginator(person, 2)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'manager.html',
                  context={
                      'person': page_obj,
                      'title': title,
                      'form': form,
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
        item.order = CartWithDict(ast.literal_eval(item.order))

    form = OrderSearch()


    paginator = Paginator(person, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'manager.html',
                  context={
                      'person': page_obj,
                      'title': title,
                      'form': form,
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


def manager_order_change(request, order_num, change):
    person = Order.objects.filter(pk=order_num).first()
    print(person.status)
    for item in person.ORDER_CHOICES:
        if item[0] == change:
            person.status = item[0]
            person.save()
            break

    return redirect(request.META.get('HTTP_REFERER'))