from django.contrib import admin
from django.urls import reverse

from .models import Order, OrderItem
from django.utils.safestring import mark_safe


class OrderItemInline(admin.TabularInline):  # привяжет список продуктов с их количеством к ордеру
    model = OrderItem
    raw_id_fields = ['product']
    extra = 0


@admin.action(description='Ссылка на заказ')  # имя столбца в таблице
def order_stripe_payment(obj):  # возвращает ссылку к ордеру на сайте stripe.com
    url = obj.get_stripe_url()
    if obj.stripe_id:
        html = f'<a href="{url}" target="_blank">{obj.stripe_id}</a>'
        return mark_safe(html)
    return ''


@admin.action(description='Товар(ы) отправленны.')
def fun_collected_sent_true(Order, request, queryset):
    queryset.update(collected_sent=True)


@admin.action(description='Отмена отправки')
def fun_collected_sent_false(Order, request, queryset):
    queryset.update(collected_sent=False)


#@admin.action(description='Накладная(чек)')
#def order_pdf(obj):
#    url = reverse('orders:admin_order_pdf', args=[obj.id])
#    return mark_safe(f'<a href="{url}">PDF</a>')  # mark_safe для экранирования символов



@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email', 'address', 'postal_code',
                    'city', 'paid', order_stripe_payment, 'collected_sent', 'created', 'updated']
    list_filter = ['paid', 'created', 'updated', ]
    inlines = [OrderItemInline]
    actions = [fun_collected_sent_true, fun_collected_sent_false]



