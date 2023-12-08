from django.shortcuts import render, HttpResponse
from products.models import Product, productCategory
# Create your views here.

# контролер - функция, которая принимает запрос и возвращает ответ или называют view или вьюха


def index(request):
    content = {
        "title": "Главная страница",
        'is_promotion': True,
    }

    return render(request, "products/index.html", content)


def products(request):
    context = {
        'title': 'Product list',
        "products": Product.objects.all(),
        "categories": productCategory.objects.all(),
    }
    return render(request, "products/products.html", context)

# {% шаблонный тег%}  {% переменная %}
