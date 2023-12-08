from django.db import models

# models = таблицы в базе данных


class productCategory(models.Model):
    def __str__(self) -> str:
        return self.name

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

    # есть 3 популярных вида удаления: CASCADE, PROTECT, SET_DEFAULT.
    # При CASCADE при удалении категории, удалятся все продукты в этой категории.
    # При PROTECT при удалении категории, будет ошибка, нельзя будет удалить категорию, пока в ней есть продукты.
    # При SET_DEFAULT при удалении категории, у всех продуктов в этой категории, будет установлена категория по умолчанию.
    category = models.ForeignKey(to=productCategory, on_delete=models.CASCADE)
