from django.contrib import admin
from .models import Order, OrderItem
from django.utils.safestring import mark_safe




@admin.action(description='Ссылка на заказ')  # имя столбца в таблице
def order_stripe_payment(obj):  # возвращает ссылку к ордеру на сайте stripe.com
    url = obj.get_stripe_url()
    if obj.stripe_id:
        html = f'<a href="{url}" target="_blank">{obj.stripe_id}</a>'
        return mark_safe(html)
    return ''


@admin.action(description='Товар(ы) отправлены.')
def fun_collected_sent_true(Order, request, queryset):
    queryset.update(collected_sent=True)


@admin.action(description='Отмена отправки')
def fun_collected_sent_false(Order, request, queryset):
    queryset.update(collected_sent=False)


@admin.display(description='Отправлено адресату') # переименование поля
def collected_sent(obj):
    return obj.collected_sent

























class OrderItemInline(admin.TabularInline):  # привяжет список продуктов с их количеством к ордеру
    model = OrderItem
    raw_id_fields = ['product']
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email', 'address', 'postal_code',
                    'city', 'paid', 'created', 'updated']
    list_filter = ['paid', 'created', 'updated', ]
    inlines = [OrderItemInline]




















