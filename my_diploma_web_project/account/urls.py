from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
from django.contrib.auth import urls
from .forms import EnterYourPasswordResetEmailForm, NewPasswordAfterReset

urlpatterns = [

    path('login/', views.user_login, name='login'),
    # path('login/<str:auto_transition>/', views.user_login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('password-change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password-change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('password-reset/', auth_views.PasswordResetView.as_view(form_class=EnterYourPasswordResetEmailForm),
         name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password-reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        form_class=NewPasswordAfterReset),
         name='password_reset_confirm'),
    path('password-reset/complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('dashboard', views.dashboard, name='dashboard'),

    # path('dashboard/<str:auto_transition>/', views.dashboard, name='dashboard'),
    # path('', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),
]
