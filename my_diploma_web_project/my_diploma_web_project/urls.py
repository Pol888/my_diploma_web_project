from django.contrib import admin

from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static







urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main_app.urls')),
    path('account/', include('account.urls')),
    path('cart/', include('cart.urls', namespace='cart')),
    path('shop/', include('shop.urls', namespace='shop')),
    path('orders/', include('orders.urls', namespace='orders')),
    path('payment/', include('payment.urls', namespace='payment')),


]

if settings.DEBUG:  # подключение media к static(вывод media через static)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
