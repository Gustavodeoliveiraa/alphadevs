from django.urls import path
from account import views

app_name = 'account'

urlpatterns = [
    path('register/', views.CreateUserView.as_view(), name='register'),
]
