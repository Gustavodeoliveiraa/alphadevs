from django.views import generic
from .models import Product
from category.models import Category


class Home(generic.ListView):
    model = Product
    template_name = 'base.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        return context
