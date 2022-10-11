from django.contrib import admin
from .models import *


class ProductTypeAdmin(admin.ModelAdmin):
    list_display = ("title", "title_extra", "slug", "order", "access")
    list_display_links = ("title",)
    list_editable = ("order", "access")
    prepopulated_fields = {"slug": ("title", "title_extra")}


class ProductAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "cost", "sales", "image", "access", "favorite")
    list_display_links = ("title", "slug", "image")
    list_editable = ("cost", "access", "favorite")
    prepopulated_fields = {"slug": ("title",)}
    filter_horizontal = ["product_type", ]


admin.site.register(ProductType, ProductTypeAdmin)
admin.site.register(Product, ProductAdmin)

