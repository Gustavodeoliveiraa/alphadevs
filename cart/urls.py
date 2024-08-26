from django.urls import path
from . import views

urlpatterns = [
    path('mycart/', views.AddToCartView.as_view(), name='mycart')
]
