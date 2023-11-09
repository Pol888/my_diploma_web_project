from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm, UserRegistrationForm
from django.contrib.auth.decorators import login_required
import time


@login_required
def dashboard(request):
    return render(request, 'account/successful_login.html', )


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Создать новый объект пользователя,
            # но пока не сохранять его
            new_user = user_form.save(commit=False)
            # Установить выбранный пароль
            new_user.set_password(
                user_form.cleaned_data['password'])
            # Сохранить объект User
            new_user.save()
            return render(request, 'account/register_done.html',
                          {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'account/register.html', {'user_form': user_form})


def user_login(request):
    massage = ''
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        massage = '✘ Данные не прошли валидацию'
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)

                    return redirect(f'dashboard')
                else:
                    massage = '✘ Аккаунт не активен, обратитесь к администратору'

            else:
                massage = '✘ Неверный логин или пароль'

    context = {'form': form, 'massage': massage}
    return render(request, 'registration/login.html', context)
