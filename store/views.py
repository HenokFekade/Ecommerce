from django.shortcuts import render, get_object_or_404
from store.models import Catagory, Product


def categories(request):
    return {'categories': Catagory.objects.all()}

def index(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'store/index.html', context)

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, in_stock=True, is_active=True)
    context = {'product': product}
    return render(request, 'store/product/detail.html', context)

def category_list(request, category_slug):
    category = get_object_or_404(Catagory, slug=category_slug)
    products = Product.objects.filter(catagory=category)
    context = {'category': category, 'products': products}
    return render(request, 'store/category.html', context)
