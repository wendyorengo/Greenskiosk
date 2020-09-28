from django.shortcuts import render, redirect
from .models import *
from .forms import ProductForm

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

def  upload_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product')
    else:
        form = ProductForm
    return render (request, 'upload_product.html', {'form': form})




    