from typing import Any
from django.views.generic import ListView
from .models import Cart, CartItem
from product.models import Category


class ListCartView(ListView):
    template_name = 'components/list_cart.html'
    model = Cart

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()

        return context
