from django.shortcuts import render,redirect
from .forms import CartForm
from catalogue.models import Product

# Create your views here.
def upload_cart(request,product_id):
    products = Product.objects.filter(id=product_id)
    if request.method == "POST":
        form = CartForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product')
    else:
        form = CartForm
        return render(request, 'cart.html', {'form':form})


    
