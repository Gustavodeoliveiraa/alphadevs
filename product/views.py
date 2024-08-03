from django.views import generic
from .models import Product
from category.models import Category


class Home(generic.ListView):
    model = Product
    paginate_by = 3
    template_name = 'components/list_products.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        return context
