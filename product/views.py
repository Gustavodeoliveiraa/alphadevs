from typing import Any
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

    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get('search')
        if search:
            queryset = Product.objects.filter(
                product_name__icontains=search
            )
        return queryset


class DetailProduct(generic.DetailView):
    model = Product
    template_name = 'detail.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context
