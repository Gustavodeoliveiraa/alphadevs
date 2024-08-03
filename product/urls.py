from django.urls import path
from .views import Home, DetailProduct

app_name = 'products'

urlpatterns = [
   path('', Home.as_view(), name='list'),
   path('detail/<int:pk>', DetailProduct.as_view(), name='detail'),
]
