from django.urls import path

from webapp.views.base import IndexView
from webapp.views.products import ProductDetailView, ProductCreateView, ProductDeleteView, ProductUpdateView

from webapp.views.cart import add_to_cart, CartView, CartProductDeleteView

from webapp.views.order import OrderCreateView

urlpatterns = [
    path('', IndexView.as_view()),
    path('products', IndexView.as_view(), name='index'),
    path('product/<int:pk>', ProductDetailView.as_view(), name='detail_product'),
    path('product/add', ProductCreateView.as_view(), name='add_product'),
    path('product/<int:pk>/delete', ProductDeleteView.as_view(), name='product_delete'),
    path('product/<int:pk>/confirm_delete', ProductDeleteView.as_view(), name='confirm_delete'),
    path('product/<int:pk>/update', ProductUpdateView.as_view(), name='product_update'),
    path('cart', CartView.as_view(), name='cart'),
    path('cart/add/<int:pk>/', add_to_cart, name='add_to_cart'),
    path('cart/<int:pk>/delete', CartProductDeleteView.as_view(), name='delete_from_cart'),
    path('cart/create_order', OrderCreateView.as_view(), name='create_order')
]
