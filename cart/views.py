import os
from django.views.generic import ListView
from django.views import View
from django.core.mail import send_mail
from .models import Product, Cart, CartItem
from django.urls import reverse_lazy, reverse
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DeleteView
from django.db.models import Sum, F
from django.contrib.auth.models import User


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
            messages.error(
                self.request,
                f"Erro ao adicionar o produto ao carrinho: {str(e)}"
            )

        return redirect(reverse_lazy('cart_list'))


class CartListView(LoginRequiredMixin, ListView):
    model = Cart
    context_object_name = 'cart'
    template_name = 'list_cart.html'

    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            messages.error(
                self.request,
                'Você deve efetuar o login para acessar o carrinho'
            )
        return super().dispatch(request, *args, **kwargs)

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


class ProcessEmail(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):

        user = User.objects.get(id=self.request.user.pk)

        products = CartItem.objects.filter(
            cart__user=self.request.user
        ).select_related('product', 'cart')

        items_link = list()

        for link in products:
            product_url = reverse('products:detail', args=[link.product.pk])
            full_path = request.build_absolute_uri(product_url)
            items_link.append(
                f'Produto: {full_path}; Quantidade {link.quantity}'
            )

        total = CartItem.objects.filter(
            cart__user=self.request.user
        ).aggregate(
            total=Sum(F('quantity') * F('product__product_price'))
        )['total'] or float(0)

        message = (
            f'Nome do suário: {user.username}\nEmail: {user.email}\n'
            + '\n'.join(items_link)
            + f'\nTotal do carrinho R$: {float(total):.2f}'
        )

        send_mail(
            'Tentativa de compra', message,
            '', [os.environ.get('EMAIL_HOST_USER')]  # type: ignore
        )

        return redirect(reverse_lazy('cart_list'))
