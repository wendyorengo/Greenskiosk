from django.shortcuts import render
from .models import *

# Create your views here.
def product_list(request):
    products = Product.objects.all()
    return render(request,'product_list.html',{'products':products})

def product(request):
    product_image = Product.objects.all()
    return render(request, 'product.html',{'product_image':product_image})

def product_details(request,product_id):
    products = Product.objects.filter(id=product_id)
    return render(request, 'details.html', {'products':products})


    