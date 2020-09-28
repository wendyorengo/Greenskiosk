from django.urls import path
from .import views
from .views import upload_kiosk

urlpatterns= [
   path('kiosk/upload/', views.upload_kiosk, name="kiosk"),
   # path('owner/upload/',upload_owner, name="owner")

]
    
