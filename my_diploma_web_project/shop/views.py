from django.shortcuts import render, get_object_or_404
from .models import Category, Product


# from my_diploma_web_project.cart.forms import CartAddProductForm


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    return render(request, 'shop/product_details.html', {'product': product})


def list_p(request, category_slug=None):
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    else:
        products = None

    return render(request, 'shop/list_p.html', {'categories': categories,
                                                'products': products, })
    # 'cart_product_form': CartAddProductForm()})

# def product_list(request, category_slug=None):
#    category = None
#    categories = Category.objects.all()
#    products = Product.objects.filter(available=True)
#    if category_slug:
#        category = get_object_or_404(Category, slug=category_slug)
#        products = products.filter(category=category)
#    return render(request, 'shop/list.html', {'category': category,
#                                                      'categories': categories,
#                                                     'products': products})
