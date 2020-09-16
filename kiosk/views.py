from django.shortcuts import render,redirect
from .forms import KioskForm
from catalogue import views

# Create your views here.
def upload_kiosk(request):
    if request.method == "Post":
        form = KioskForm(request.POST, request.FIles)
        if form.is_valid():
            form.save()
            return redirect('product')
    else:
        form = KioskForm
        return render(request, 'kiosk_upload.html', {'form':form})

def upload_owner(request):
    if request.method == "Post":
        form = KioskownerForm(request.POST, request.Files)
        if form.is_valid():
            form.save()
            return redirect('product')
    else:
        form = KioskownerForm
        return render(request, 'kioskowner.html', {'form':form})
            

