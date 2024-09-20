from django.urls import path
from . import views

urlpatterns = [
  add_at_cart
    path('mycart/', views.AddToCartView.as_view(), name='mycart'),
    path('mycart/list', views.CartListView.as_view(), name='cart_list'),
    path(
        'mycart/delete/<int:pk>/',
        views.CartDeleteView.as_view(),
        name='cart_delete'
    ),
    path('send_mail', views.ProcessEmail.as_view(), name='send_email')
]
