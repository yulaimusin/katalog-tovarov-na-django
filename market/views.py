from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Category, Product


def product_list_homepage(request):
    categories = Category.objects.all()
    products = Product.objects.filter(in_stock__gt=0)
    context = {"categories": categories, "products": products}
    return render(request, "market/product_list_homepage.html", context=context)


def product_list(request, category_slug=None):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category, in_stock__gt=0)
    context = {"category": category, "products": products}
    return render(request, "market/product_list.html", context=context)


def product_details(request, category_slug=None, product_id=None, product_slug=None):
    product = get_object_or_404(Product, id=product_id)
    if product.category.slug != category_slug or product.slug != product_slug:
        raise Http404
    context = {"product": product}
    return render(request, "market/product_details.html", context=context)
