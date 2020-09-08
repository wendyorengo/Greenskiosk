from django.urls import path
from .views import product_list,product

urlpatterns= [
    path('products/', product_list, name="product-list"),
    path('image/', product, name="product")

]
    


