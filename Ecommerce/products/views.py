from django.shortcuts import render
def products(requrst):
    return render (requrst,'products/products.html')

def product(requrst):
    return render (requrst,'products/product.html')