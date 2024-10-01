from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic
from account.forms import FormUserCreation
from django.contrib.auth.views import LoginView
from product.models import Category
from django.contrib.auth import logout, login, authenticate
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
        form = super().form_valid(form)

        user = authenticate(
            self.request,
            username=self.request.POST['username'],
            password=self.request.POST['password1'],
        )
        login(self.request, user)
        return form

    def form_invalid(self, form):
        response = super().form_invalid(form)
        return response


class LoginUserView(LoginView):
    success_url = reverse_lazy('products:list')
    template_name = 'components/login.html'

    def form_valid(self, form):
        messages.success(self.request, 'Login efetuado com sucesso !')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Email ou Senha Errados')
        return super().form_invalid(form)


def logout_view(request):
    logout(request)
    return redirect('products:list')
