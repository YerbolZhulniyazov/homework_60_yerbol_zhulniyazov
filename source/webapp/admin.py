from django.contrib import admin

from webapp.models import Product, Order, OrderProducts


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'image', 'category', 'remaining', 'price', 'is_deleted', 'deleted_at')
    list_filter = ('id', 'name', 'category', 'price', 'remaining', 'is_deleted', 'deleted_at')
    search_fields = ('id', 'category', 'description', 'remaining', 'price')
    fields = ('id', 'name', 'category', 'description', 'price', 'remaining', 'image')
    readonly_fields = ('id',)


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'phone_number', 'address', 'created_at')
    list_filter = ('products', 'username', 'phone_number', 'address', 'created_at')
    search_fields = ('products', 'username', 'phone_number', 'address')
    fields = ('id', 'username', 'phone_number', 'address')
    readonly_fields = ('id',)
    ordering = ('-created_at',)


class OrderProductsAdmin(admin.ModelAdmin):
    list_display = ('product', 'order', 'amount')
    list_filter = ('product', 'order', 'amount')


admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderProducts, OrderProductsAdmin)
