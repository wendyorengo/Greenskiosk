from django.urls import path
from .import views
from .views import upload_cart

urlpatterns= [
    path('basket/',upload_cart, name="cart")

]