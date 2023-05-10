from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from django.views.decorators.http import require_POST
from django.http import JsonResponse

from products.models import ProductCard
from cart.models import UserCart

def about(request):
    return render(request, 'about.html')

def location(request):
    return render(request, 'location.html')

def menu_page(request):
    products = ProductCard.objects.all()
    categories = []
    for product in products:
        if product.category not in categories:
            categories.append(product.category)

    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {
        'categories': categories,
        'products': products,
    }

    return render(request, 'menu_page.html', context)

def catering(request):
    return render(request, 'catering.html')

def reviews(request):
    return render(request, 'reviews.html')