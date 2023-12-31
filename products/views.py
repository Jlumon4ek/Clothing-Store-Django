from django.core.paginator import Paginator
from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from products.models import Product, productCategory, Basket
from users.models import Users
from django.contrib.auth.decorators import login_required

# Create your views here.

# контролер - функция, которая принимает запрос и возвращает ответ или называют view, или вьюха


def index(request):
    content = {
        "title": "Главная страница",
        'is_promotion': True,
    }

    return render(request, "products/index.html", content)


def products(request, category_id=None, page_number=1):
    product = Product.objects.filter(
        category__id=category_id) if category_id else Product.objects.all()

    per_page = 2
    paginator = Paginator(product, per_page)
    products_paginator = paginator.page(page_number)

    context = {
        'title': 'Product list',
        "products": products_paginator,
        "categories": productCategory.objects.all(),
    }
    return render(request, "products/products.html", context)


# {% шаблонный тег%} {% переменная %}
@login_required
def basket_add(request, product_id):
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, products=product)

    if not baskets.exists():
        Basket.objects.create(user=request.user, products=product, quantity=1)
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def basket_remove(request, product_id):
    basket = Basket.objects.get(id=product_id)
    basket.delete()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])
