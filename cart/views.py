from django.views import View
from .models import Product, Cart, CartItem
from django.urls import reverse
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin


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
                    self.request, "Produto adicionado ao carrinho com sucesso!"
                )

        except Exception as e:
            messages.success(
                self.request,
                f"Erro ao adicionar o produto ao carrinho: {str(e)}"
            )

        return redirect(reverse('products:detail', args=[product_id]))
