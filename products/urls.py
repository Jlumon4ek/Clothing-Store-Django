
from django.urls import path
from products.views import *

app_name = 'products'

urlpatterns = [
    # где мы передавали например в href = "index.html" будем передавать href="{% url 'index' %}" в .html файле?
    path('', products, name='index'),
    path('products/<int:category_id>/', products, name='category'),
    path('baskets/add/<int:product_id>/', basket_add, name='basket_add'),
    path('baskets/remvoe/<int:product_id>/',
         basket_remove, name='basket_remove'),
    path('page/<int:page_number>/', products, name='paginator'),

]
