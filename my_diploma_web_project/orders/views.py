from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import OrderItem, Order
from .forms import OrderCreateForm
from cart.cart import Cart
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import render_to_string




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

            request.session['order_id'] = order.id # создает id ордера для оплаты в сеансе
            # перенаправить к платежу
            return redirect(reverse('payment:process'))  # ввод платежных данных
    else:
        form = OrderCreateForm()
    return render(request, 'orders/create.html', {'cart': cart, 'form': form})


#from django.shortcuts import render
#from django.http import HttpResponse
#from xhtml2pdf import pisa


#def generate_invoice_pdf(request, order_id):
#    # Получение данных о заказе из базы данных или другого источника
#    #order = Order.objects.get(id=order_id)
#
#    # Заполнение данных в HTML-шаблоне
#    html = render(request, 'orders/pdf.html', {'order': order}).content
#
#    # Создание временного файла для сохранения PDF
#    pdf_file = 'ppp.pdf'
#
#    # Преобразование HTML в PDF
#    with open(pdf_file, 'wb') as f:
#        pisa.CreatePDF(html, dest=f)
#
#    # Отправка PDF-файла в ответе
#    with open(pdf_file, 'rb') as f:
#        response = HttpResponse(f.read(), content_type='application/pdf')
#        response['Content-Disposition'] = 'attachment; filename="invoice.pdf"'
#        return response




#from django.conf import settings
#from django.http import HttpResponse
#from django.template.loader import render_to_string
## генерация чека pdf // import weasyprint
#@staff_member_required # доступ только для штатных пользователей
#def admin_order_pdf(request, order_id):
#    order = get_object_or_404(Order, id=order_id)
#    html = render_to_string('orders/pdf.html',{'order': order}) # прорисовка шаблона
#
#    response = HttpResponse(content_type='application/pdf')
#    response['Content-Disposition'] = f'filename=order_{order.id}.pdf' # задается имя
#    weasyprint.HTML(string=html).write_pdf(response, # генерация pdf с помощью  weasyprint с подключением css
#                                           stylesheets=[weasyprint.CSS(settings.STATICFILES_DIRS[0] / 'css/pdf.css')])
#    return response