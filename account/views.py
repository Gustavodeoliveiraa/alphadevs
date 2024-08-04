from django.urls import reverse_lazy
from django.views import generic
from account.forms import FormUserCreation


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
