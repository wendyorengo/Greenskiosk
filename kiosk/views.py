from django.shortcuts import render,redirect
from .forms import KioskForm
from catalogue.views import upload_product


# Create your views here.
def  upload_kiosk(request):
    if request.method == 'POST':
        form = KioskForm(request.POST, request.FILES)
        
        if form.is_valid():
            form.save()
        return redirect('uploads')
    else:
        form = KioskForm
        return render (request, 'kiosk_upload.html', {'form': form})



