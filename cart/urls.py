from django.urls import path
from . import views

urlpatterns = [
    path('mycart/', views.ListCartView.as_view(), name='mycart')
]
