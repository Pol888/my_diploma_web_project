from django.shortcuts import render, redirect
from django.urls import reverse
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart
from django.core.mail import send_mail




def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order, product=item['product'], price=item['price'],
                                         quantity=item['quantity'])
            cart.clear()

            subject = f'Номер заказа {order.id}'
            message = f'Уважаемый {order.first_name},\n\n' \
                      f'Вы оформили заказ на нашем сайте.' \
                      f'Номер вашего заказа: {order.id}.'
            # отправляет сообщение после успешного оформления заказа
            send_mail(subject, message,
                      'dpa777@inbox.com',
                      [order.email])

            request.session['order_id'] = order.id  # создает id ордера для оплаты в сеансе
            # перенаправить к платежу
            return redirect(reverse('payment:process'))  # ввод платежных данных
    else:
        form = OrderCreateForm()
    return render(request, 'orders/create.html', {'cart': cart, 'form': form})






