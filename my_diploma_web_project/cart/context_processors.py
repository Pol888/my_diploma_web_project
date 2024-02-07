from .cart import Cart


def cart(request):  # процессор контекста
    return {'cart': Cart(request)}
