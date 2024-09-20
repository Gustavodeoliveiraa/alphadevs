from django.http import HttpRequest, HttpResponse
from django.views import View
from .models import Product, Cart, CartItem
from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from django.views.generic import DeleteView
from django.db.models import Sum, F


class AddToCartView(LoginRequiredMixin, View):
    def post(self, *args, **kwargs):
        product_id = self.request.POST.get('id_product')
        product = get_object_or_404(Product, id=product_id)

        user_cart = Cart.objects.get(user=self.request.user)

        cart_item, created = CartItem.objects.get_or_create(
            cart=user_cart, product=product,
        )

        try:
            if not created:
                cart_item.quantity += 1
                cart_item.save()
            messages.success(
                self.request, "Produto adicionado ao carrinho com sucesso!",
            )

        except Exception as e:
            messages.success(
                self.request,
                f"Erro ao adicionar o produto ao carrinho: {str(e)}"
            )

        return redirect(reverse_lazy('cart_list'))


class CartListView(LoginRequiredMixin, ListView):
    model = Cart
    context_object_name = 'cart'
    template_name = 'list_cart.html'

    def get_queryset(self):
        query = super().get_queryset()
        query = CartItem.objects.filter(
            cart__user=self.request.user
        ).order_by('-id').select_related('product', 'cart')

        return query

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['total'] = CartItem.objects.filter(
            cart__user=self.request.user
        ).aggregate(
            total=Sum(F('quantity') * F('product__product_price'))
        )['total'] or float(0)
        return context


class CartDeleteView(LoginRequiredMixin, DeleteView):
    model = CartItem
    success_url = reverse_lazy('cart_list')

    def post(self, request, *args, **kwargs):
        cart_item = self.get_object()
        messages.error(
            self.request,
            f'Produto "{cart_item.product.product_name}" Removido com sucesso'
        )
        return super().post(request, *args, **kwargs)
