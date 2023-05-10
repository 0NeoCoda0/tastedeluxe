from django.contrib import admin

from .models import ProductCard

class ProductCardAdmin(admin.ModelAdmin):
    list_display = ('name', 'food_type', 'category')
    search_fields = ('name', 'food_type', 'category')

admin.site.register(ProductCard, ProductCardAdmin)


# Register your models here.
