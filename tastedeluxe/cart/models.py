from django.db import models

from tastedeluxe.settings import AUTH_USER_MODEL

from products.models import ProductCard

class UserCart(models.Model):
    user = models.OneToOneField(AUTH_USER_MODEL, on_delete=models.CASCADE) 
    items = models.ManyToManyField(ProductCard, through='CartItem')

    def add_to_cart(self, product):
        item, created = CartItem.objects.get_or_create(cart=self, product=product)
        if not created:
            item.quantity += 1
            item.save()
    
    def remove_from_cart(self, product):
        item = CartItem.objects.get(cart=self, product=product)
        item.delete()
    
    def get_total_price(self):
        items = self.cartitem_set.all()
        return sum(item.get_total_price() for item in items)

class CartItem(models.Model):
    cart = models.ForeignKey(UserCart, on_delete=models.CASCADE)
    product = models.ForeignKey(ProductCard, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def get_total_price(self):
        return self.product.price * self.quantity