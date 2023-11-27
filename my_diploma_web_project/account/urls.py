from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
from django.contrib.auth import urls
from .forms import EnterYourPasswordResetEmailForm, NewPasswordAfterReset

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    path('password-reset/', auth_views.PasswordResetView.as_view(form_class=EnterYourPasswordResetEmailForm,
                                                                 template_name="account/password_reset_form.html",
                                                            email_template_name="account/password_reset_email.html"),
         name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name=
                                                                          "account/password_reset_done.html"),
         name='password_reset_done'),
    path('password-reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name=
                                                                                "account/password_reset_confirm.html",
                                                                                    form_class=NewPasswordAfterReset),
         name='password_reset_confirm'),
    path('password-reset/complete/', auth_views.PasswordResetCompleteView.as_view(template_name=
                                                                                "account/password_reset_complete.html"),
         name='password_reset_complete'),
    path('successful_login', views.successful_login, name='successful_login'),

    # path('password-change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    # path('password-change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    # path('', include('django.contrib.auth.urls')),

]

a = input()
if a != 5:
    print(4)
else:
    print(1)