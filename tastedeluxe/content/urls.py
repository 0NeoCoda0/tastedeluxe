from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu_page, name='menu_page'),
    path('about/', views.about, name='about'),
    path('location/', views.location, name='location'),
    path('catering/', views.catering, name='catering'),
    path('reviews/', views.reviews, name='reviews'),
]