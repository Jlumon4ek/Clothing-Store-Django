from django.db import models
from users.models import Users

# Есть 3 популярных вида удаления: CASCADE, PROTECT, SET_DEFAULT.
# При CASCADE при удалении категории, удалятся все продукты в этой категории.
# При PROTECT при удалении категории, будет ошибка, нельзя будет удалить категорию, пока в ней есть продукты.
# При SET_DEFAULT при удалении категории, у всех продуктов в этой категории, будет установлена категория по умолчанию.

# models = таблицы в базе данных


class productCategory(models.Model):
    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    name = models.CharField(max_length=128, unique=True)
    description = models.TextField(null=True, blank=True)


class Product(models.Model):
    def __str__(self) -> str:
        return f"Product: {self.name} | Category: {self.category.name}"

    name = models.CharField(max_length=256)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    img = models.ImageField(upload_to='products_images', blank=True)
    category = models.ForeignKey(to=productCategory, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"


class BasketQuerySet(models.QuerySet):
    def total_sum(self):
        return sum(basket.sum() for basket in self)

    def total_quantity(self):
        return sum(basket.quantity for basket in self)


class Basket(models.Model):
    def __str__(self) -> str:
        return f"Basket: {self.id}"

    user = models.ForeignKey(to=Users, on_delete=models.CASCADE)
    products = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    objects = BasketQuerySet.as_manager()

    def sum(self):
        return self.quantity * self.products.price

    class Meta:
        verbose_name = "Basket"
        verbose_name_plural = "Baskets"
