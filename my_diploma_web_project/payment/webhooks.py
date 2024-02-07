import stripe
from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from orders.models import Order



@csrf_exempt # предотвращает валидацию CSRF
def stripe_webhook(request):
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None
    try:
        # верификация заголовка подписи с сервера stripe(для предотвращения подложных данных)
        event = stripe.Webhook.construct_event(payload,sig_header,settings.STRIPE_WEBHOOK_SECRET)
    except ValueError as e:
       # Недопустимая полезная нагрузка
       return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Недопустимая подпись
        return HttpResponse(status=400)
    # все в порядке
    # при удачной оплате заказа, ордер помечается как оплаченный
    if event.type == 'checkout.session.completed':
        session = event.data.object
        if session.mode == 'payment' and session.payment_status == 'paid':
            try:
                order = Order.objects.get(id=session.client_reference_id)
            except Order.DoesNotExist:
                return HttpResponse(status=404)
            # помечает заказ как оплаченный
            order.paid = True
            # сохраняет ID платежа Stripe
            order.stripe_id = session.payment_intent
            order.save()
            #render('orders:invoice/<int:order_id>/pdf/'
            #generate_invoice_pdf(request, order.id)
    return HttpResponse(status=200)