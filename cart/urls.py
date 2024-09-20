from django.urls import path
from . import views

urlpatterns = [
  add_at_cart
    path('mycart/', views.AddToCartView.as_view(), name='mycart'),
    path('mycart/list', views.CartListView.as_view(), name='cart_list'),
  master
]
