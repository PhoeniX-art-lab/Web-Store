from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.views.generic import FormView
from django.core.mail import send_mail
from django.conf import settings
import copy

from store.models import Store
from .cart import Cart
from .forms import CartAddProductForm, CartOrderForm


@require_POST
def cart_add(request, product_id):
    """Add products to cart"""
    cart = Cart(request)
    product = get_object_or_404(Store, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return redirect('cart:cart_detail')


def cart_remove(request, product_id):
    """Remove product from cart"""
    cart = Cart(request)
    product = get_object_or_404(Store, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'],
                                                                   'update': True})
    return render(request, 'cart/detail.html', {'cart': cart, 'title': 'Cart'})


class CartOrder(FormView):
    form_class = CartOrderForm
    template_name = 'cart/order.html'

    def get_context_data(self, **kwargs):
        context = super(CartOrder, self).get_context_data(**kwargs)
        return context | {'title': 'Order'}

    def post(self, request, *args, **kwargs):
        user_data = request.POST.dict()
        user_data.pop('csrfmiddlewaretoken', None)
        cart = Cart(request)
        order = []
        for item in cart:
            order.append(item)
        for item in order:
            product = Store.objects.filter(product_name=item['product']).first()
            cart.remove(product)
        order.append(copy.deepcopy(user_data))
        print(order)
        send_mail(f"Order from {user_data['name']}", str(order), settings.DEFAULT_FROM_EMAIL, settings.RECIPIENTS_EMAIL)
        return render(request, 'cart/order_success.html', {"detail": order})
