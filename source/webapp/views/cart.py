from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView

from webapp.forms import OrderForm
from webapp.models import ProductInCart, Product


def add_to_cart(request, pk):
    product = get_object_or_404(Product, pk=pk)
    cart_product = ProductInCart.objects.filter(product=product.pk)
    if len(cart_product) == 0 and product.remaining > 0:
        data = {
            'product': product,
            'amount': 1
        }
        ProductInCart.objects.create(**data)
    elif len(cart_product) != 0:
        if cart_product[0].amount < product.remaining:
            cart_product = get_object_or_404(ProductInCart, pk=cart_product[0].pk)
            cart_product.amount += 1
            cart_product.save()
    return redirect('index')


class CartView(ListView):
    model = ProductInCart
    template_name = 'cart.html'
    context_object_name = 'products_in_cart'
    queryset = ProductInCart.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        total_count = 0
        total = 0
        for product_cart in ProductInCart.objects.all():
            total += product_cart.product.price * product_cart.amount
            total_count += product_cart.amount
        context['total'] = total
        context['total_count'] = total_count
        context['form'] = OrderForm
        return context


class CartProductDeleteView(DeleteView):
    model = ProductInCart
    template_name = 'cart.html'
    success_url = reverse_lazy('cart')
    queryset = ProductInCart.objects.all()

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)
