from django.contrib import admin
from .models import *


class ProductTypeAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "order", "access")
    list_display_links = ("title",)
    list_editable = ("order", "access")
    prepopulated_fields = {"slug": ("title",)}


class ProductAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "image", "access", "favorite",)
    list_display_links = ("title", "slug", "image")
    list_editable = ("access", "favorite")
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(ProductType, ProductTypeAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductSubtype)
admin.site.register(ProductExtra)
