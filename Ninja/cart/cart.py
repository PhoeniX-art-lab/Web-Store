from django.conf import settings
from store.models import Store


class Cart(object):
    """Class that realised a cart on sessions"""

    def __init__(self, request):
        """Initialised cart"""
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # save an empty cart in the session
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def __iter__(self):
        """Iterating through the items in the cart and getting the products from the database"""
        product_ids = self.cart.keys()
        products = Store.objects.filter(id__in=product_ids)

        for product in products:
            self.cart[str(product.id)]['product'] = product

        for item in self.cart.values():
            item['price'] = int(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        """Count all products in cart"""
        return sum(item['quantity'] for item in self.cart.values())

    def add(self, product, quantity=1, update_quantity=False):
        """Add product to cart or update its quantity"""
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {
                'quantity': 0,
                'price': str(product.product_price)
            }

        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()

    def get_total_price(self):
        """Calculate the cost of items in the shopping cart"""
        return sum(item['quantity'] * int(item['price']) for item in self.cart.values())

    def save(self):
        # Update cart session
        self.session[settings.CART_SESSION_ID] = self.cart

        # Mark the session as "modified" to make sure it's saved
        self.session.modified = True

    def remove(self, product):
        """Removing product from cart"""
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def clear(self):
        """Delete cart from session"""
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True
