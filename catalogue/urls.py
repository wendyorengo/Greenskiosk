from django.urls import path
from .views import product_list, product, product_details,upload_product

urlpatterns= [
    path('product/', product_list, name="product-list"),
    path('', product, name="product"),
    path('products/<int:product_id>/',product_details, name="detail"),
    path('products/upload/', upload_product, name="uploads")

]
    


