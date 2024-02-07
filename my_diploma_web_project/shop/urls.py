from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('<slug:category_slug>/', views.list_p,
         name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
    path('', views.list_p, name='list_p'),

]
