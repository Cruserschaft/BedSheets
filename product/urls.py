from django.urls import *
from .views import *

urlpatterns = [
    path('', start_product, name='product'),
    path('item/<slug:item_slug>/', item_page, name='product_item'),
    path('<slug:post_slug>/', product_slug, name='product_category'),
    path('<slug:post_slug>/<slug:post_type_slug>', product_type_slug, name='product_type_category'),
]