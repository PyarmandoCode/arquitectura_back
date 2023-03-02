from django.urls import path
from .views import ProductosList

#Endpoint

urlpatterns = [
    path("api/productosall/",ProductosList.as_view())
]
