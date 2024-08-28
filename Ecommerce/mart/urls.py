from django.urls import path
from . import views

urlpatterns = [
    path('', views.display_form, name='display_form'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
]
