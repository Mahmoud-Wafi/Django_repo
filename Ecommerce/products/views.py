from django.shortcuts import render
from .models import Product
from .serializers import ProductSerializer
from rest_framework.decorators import api_view 
from rest_framework.response import Response


def product(requrst):
    return render (requrst,'products/product.html')

@api_view (['GET','POST'])
def products(request):
    if request.method=="GET":
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    
    
# def view_products(request):
#     response = requests.get('http://localhost:8001/api/products/')  # Adjust URL as needed
#     products = response.json()
#     return render(request, 'products/products.html', {'products': products})


     

               