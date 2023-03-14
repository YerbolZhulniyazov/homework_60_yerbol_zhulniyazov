from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView

from webapp.forms import ProductForm
from webapp.models import Product


class ProductDetailView(DetailView):
    template_name = 'product.html'
    model = Product


class ProductCreateView(CreateView):
    template_name = 'product_add.html'
    model = Product
    form_class = ProductForm

    def get_success_url(self):
        return reverse('detail_product', kwargs={'pk': self.object.pk})


class ProductUpdateView(UpdateView):
    template_name = 'product_update.html'
    form_class = ProductForm
    model = Product

    def get_success_url(self):
        return reverse('detail_product', kwargs={'pk': self.object.pk})


class ProductDeleteView(DeleteView):
    template_name = 'confirm_delete.html'
    model = Product
    context_object_name = 'product'
    success_url = reverse_lazy('index')
