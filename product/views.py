from django.http import HttpResponse
from django.shortcuts import render
from .models import *


def start_product(request):
    category = ProductType.objects.filter(title_extra=None, access=True)
    products = Product.objects.filter(access=True)
    return render(request, 'product.html',
                  context={
                      "category": category,
                      "products": products,
                  })


def product_slug(request, post_slug):
    category = ProductType.objects.filter(title_extra=None, access=True)
    category_type = ProductType.objects.filter(access=True, slug__startswith=post_slug).exclude(slug__iexact=post_slug)
    products = Product.objects.filter(product_type__slug=post_slug)
    print(products)
    return render(request, 'product.html',
                  context={
                      "category": category,
                      "products": products,
                      "category_type": category_type,
                  })


def product_type_slug(request, post_slug, post_type_slug):
    category = ProductType.objects.filter(title_extra=None, access=True)
    category_type = ProductType.objects.filter(access=True, slug__startswith=post_slug).exclude(slug__iexact=post_slug)
    products = Product.objects.filter(product_type__slug=post_type_slug)
    print(products)
    return render(request, 'product.html',
                  context={
                      "category": category,
                      "products": products,
                      "category_type": category_type,
                  })


def item_page(request, item_slug):
    item = Product.objects.filter(access=True, slug=item_slug)[0]
    item_type = item.product_type.filter(title_extra__isnull=False)

    return render(request, 'single-product.html',
                  context={
                      "prod_item": item,
                      "prod_item_type": item_type,
                  })
