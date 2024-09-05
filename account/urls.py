from django.urls import path
from account import views

app_name = 'account'

urlpatterns = [
    path('login/', views.LoginUserView.as_view(), name='login'),
    path('register/', views.CreateUserView.as_view(), name='register'),
    path('logout/', views.logout_view, name='logout'),

]
