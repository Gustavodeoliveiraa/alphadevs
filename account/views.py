from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic
from account.forms import FormUserCreation
from django.contrib.auth.views import LoginView


class CreateUserView(generic.CreateView):
    form_class = FormUserCreation
    template_name = 'components/register.html'
    success_url = reverse_lazy('products:list')

    def form_valid(self, form):
        print('form validado')
        return super().form_valid(form)

    def form_invalid(self, form):
        response = super().form_invalid(form)
        print('form invalido')
        return response


class LoginUserView(LoginView):
    success_url = reverse_lazy('products:list')
    template_name = 'components/register.html'

    def form_valid(self, form):
        print('autenticado')
        return super().form_valid(form)

    def form_invalid(self, form):
        super().form_invalid(form)
        print('Login ou Senha ERRADAS')
        return redirect('products:list')