from django.shortcuts import render, HttpResponse

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
        "products": [
            {
                'img': "/static/vendor/img/products/Adidas-hoodie.png",
                'name': 'Adidas hoodie',
                "price": 6090,
                "description": "Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни",
            },
            {
                'img': "/static/vendor/img/products/Blue-jacket-The-North-Face.png",
                'name': 'Синяя куртка The North Face',
                "price": 23725,
                "description": "Гладкая ткань. Водонепроницаемое покрытие. Легкий и теплый пуховый наполнитель.",
            },
            {
                'img': "/static/vendor/img/products/Adidas-hoodie.png",
                'name': 'Adidas hoodie',
                "price": 6090,
                "description": "Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни",
            }
        ]
    }
    return render(request, "products/products.html", context)

# {% шаблонный тег%}  {% переменная %}
