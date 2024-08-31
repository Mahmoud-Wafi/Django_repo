# orders/views.py
from django.shortcuts import render
from .serializers import OrderSerializer
from .models import Order
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view (['GET','POST'])
def order_view(request):
    if request.method =="GET":
         orders= Order.objects.all()
         serializer=OrderSerializer(orders, many=True)
         return Response(serializer.data)
        
    

