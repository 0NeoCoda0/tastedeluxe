from django.contrib import admin

from .models import CartItem, UserCart

class CartAdmin(admin.ModelAdmin):
    list_display = ('user', )

class CartItemAdmin(admin.ModelAdmin):
    list_display = ('cart', 'product', 'quantity')

admin.site.register(CartItem, CartItemAdmin)
admin.site.register(UserCart, CartAdmin)
