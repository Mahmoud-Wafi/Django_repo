import pandas as pd
from django.shortcuts import render, get_object_or_404 ,redirect
from products.models import Product 

def display_form(request):
    context={
        "products":Product.objects.all()
    }
    return render(request, 'mart/display_form.html', context)

def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'mart/product_detail.html', {'product': product})


def cart(request,id):
    product = get_object_or_404(Product, id=id)
    cart = request.session.get('cart', {})
    
    if str(id) in cart:
        cart[str(id)]['quantity'] += 1
    else:
        cart[str(id)] = {
            'productName': product.name,
            'price': str(product.price),
            'quantity': 1,
            'image_url': product.image.url
        }
    
    request.session['cart'] = cart
    return redirect('display_form')

def view_cart(request):
    cart = request.session.get('cart', {})
    total_price = 0
    for item in cart.values():
        total_price += float(item['price']) * item['quantity']
    
    context = {
        'cart': cart,
        'total_price': total_price
    }
    return render(request, 'mart/view_cart.html', context)

def remove_from_cart(request,id):
    cart = request.session.get('cart', {})
    
    if str(id) in cart:
        del cart[str(id)]
        request.session['cart'] = cart
    return redirect('view_cart')
