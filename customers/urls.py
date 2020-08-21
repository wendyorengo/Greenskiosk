import . from customers
from django import path

urlpatterns = [
    path("", admin.site.urls),
]