from django.urls import path
from . import views

urlpatterns = [
    path('', views.display_form, name='display_form'),
    path('product/<int:id>/', views.product_detail, name='product_detail'),
    path('cart/<int:id>/', views.cart, name='cart'),
    path('view_cart/', views.view_cart, name='view_cart'),
     path('remove_from_cart/<int:id>/', views.remove_from_cart, name='remove_from_cart'),
    
]


