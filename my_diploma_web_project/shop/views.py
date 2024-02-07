from django.shortcuts import render, get_object_or_404
from cart.forms import CartAddProductForm
from .models import Category, Product



def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    return render(request, 'shop/product_details.html', {'product': product,
                                                         'cart_product_form': CartAddProductForm()})


def list_p(request, category_slug=None):
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    else:
        products = None

    return render(request, 'shop/list_p.html', {'categories': categories, 'products': products, })



