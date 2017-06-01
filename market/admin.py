from django.contrib import admin
from .models import Category, Product


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    list_display_links = ['title']
    list_editable = []
    list_filter = []
    search_fields = ['title']
    prepopulated_fields = {'slug': ('title', )}

    class Meta:
        model = Category


class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'price', 'in_stock', 'created', 'updated']
    list_display_links = ['title']
    list_filter = ['category', 'price', 'in_stock', 'updated']
    list_editable = ['price', 'in_stock']
    prepopulated_fields = {'slug': ('title', )}

    class Meta:
        model = Product

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
