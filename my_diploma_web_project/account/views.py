# from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm, UserRegistrationForm
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(
                user_form.cleaned_data['password'])
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
        massage = 'Данные не прошли валидацию'
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect(f'successful_login')
                else:
                    massage = 'Аккаунт не активен, обратитесь к администратору'
            else:
                massage = 'Неверный логин или пароль'

    context = {'form': form, 'massage': massage}
    return render(request, 'account/login.html', context)


@login_required
def successful_login(request):
    return render(request, 'account/successful_login.html', )
