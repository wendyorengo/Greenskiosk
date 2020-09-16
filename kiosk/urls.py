from django.urls import path
from .import views
from .views import upload_kiosk, upload_owner

urlpatterns= [
   path('kiosk/upload/', upload_kiosk, name="kiosk"),
   path('owner/upload/',upload_owner, name="owner")

]
    
