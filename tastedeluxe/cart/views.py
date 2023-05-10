from django.shortcuts import get_object_or_404, render
from django.views.decorators.http import require_POST
from django.http import JsonResponse

from .models import UserCart
from products.models import ProductCard

def user_cart(request):
    cart = get_object_or_404(UserCart, user=request.user)
    cart_items = cart.cartitem_set.all()
    context = {
        'cart': cart,
        'cart_items': cart_items,

    }
    return render(request, 'usercart.html' ,context)

@require_POST
def add_to_cart(request, product_id):
    product = get_object_or_404(ProductCard, id=product_id)
    cart, created = UserCart.objects.get_or_create(user=request.user)
    cart.add_to_cart(product)
    return JsonResponse({'success': True})