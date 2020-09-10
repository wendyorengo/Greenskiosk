from django.urls import path
from .views import product_list,product,product_details

urlpatterns= [
    path('products/', product_list, name="product-list"),
    path('image/', product, name="product"),
    path('products/<int:product_id>/', product_details, name="detail")

]
    


