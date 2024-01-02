from django.contrib import admin
from products.models import Product, productCategory, Basket
# Register your models here.

admin.site.register(productCategory)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'category')
    fields = (('name', 'quantity'), 'description',
              ('price', 'category'), 'img')

    readonly_fields = ('description',)
    search_fields = ('name',)
    # ordering = ('name',)


class BasketAdmin(admin.TabularInline):
    model = Basket
    fields = ('products', 'quantity', 'created_at')
    readonly_fields = ('created_at', )
    extra = 0
