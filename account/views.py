from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic
from account.forms import FormUserCreation
from django.contrib.auth.views import LoginView
from product.models import Category
from django.contrib.auth import logout
from django.contrib import messages


class CreateUserView(generic.CreateView):
    form_class = FormUserCreation
    template_name = 'components/register.html'
    success_url = reverse_lazy('products:list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        return context

    def form_valid(self, form):
        messages.success(self.request, 'Cadastro concluído com sucesso')
        return super().form_valid(form)

    def form_invalid(self, form):
        response = super().form_invalid(form)
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


def logout_view(request):
    logout(request)
    return redirect('products:list')