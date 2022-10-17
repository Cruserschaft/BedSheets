from product.models import *
from django.conf import settings


class Cart:
    def __init__(self, request):
        self.session = request.session

        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}

        self.cart = cart
        print(self.cart)

    def extra_add(self, product, extra_num):
        product_id = str(product.id)
        self.cart[product_id][f'extra{extra_num}'] = True
        self.save()

    def extra_remove(self, product, extra_num):
        product_id = str(product.id)
        num = str(extra_num)
        if f'extra{extra_num}' in self.cart[product_id]:
            del self.cart[product_id][f'extra{extra_num}']
        self.save()


    def add(self, product, quantity=1, update_quantity=False, sub=False):
        product_id = str(product.id)

        if product_id not in self.cart:
            self.cart[product_id] = {"quantity": 0, }

        if update_quantity:
            self.cart[product_id]["quantity"] = quantity
        else:
            if not sub:
                self.cart[product_id]["quantity"] += quantity
            else:
                self.cart[product_id]["quantity"] -= quantity
        self.save()

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __iter__(self):
        product_ids = self.cart.keys()

        products = ProductSubtype.objects.filter(id__in=product_ids)

        cart = self.cart.copy()

        for product in products:
            cart[str(product.id)]['product'] = product

        for item in cart.values():
            item['total_price'] = item['product'].cost * item['quantity']
            yield item

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.save()

    def get_total_price(self):
        res_extra = 0
        res_all = sum(item['total_price'] for item in self.cart.values())

        for item in self.cart.values():
            if "extra1" in item:
                res_extra += (item['product'].parent.extra1.cost * item['quantity'])
            if "extra2" in item:
                res_extra += (item['product'].parent.extra2.cost * item['quantity'])
            if "extra3" in item:
                res_extra += (item['product'].parent.extra3.cost * item['quantity'])
        return {"all": res_all+res_extra, "extra": res_extra, "products": res_all}

    def save(self):
        self.session.modified = True
