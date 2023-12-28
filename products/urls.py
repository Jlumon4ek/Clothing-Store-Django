
from django.urls import path
from products.views import *

app_name = 'products'

urlpatterns = [
    # где мы передавали например в href = "index.html" будем передавать href="{% url 'index' %}" в .html файле?
    path('', products, name='index'),
    path('baskets/add/<int:product_id>/', basket_add, name='basket_add'),
    path('baskets/remvoe/<int:product_id>/', basket_remove, name='basket_remove'),
]


