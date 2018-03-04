# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, UserModel
from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.http import HttpResponseRedirect
from django.contrib.auth.views import login as auth_views_login


def user_login(request):
    """
    Login an original user user
    :param request:
    :return:
    """
    context = {
        'auth_views_login': auth_views_login,
    }

    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('/')
    return render(request, 'users/user_login.html', context)


def user_signup(request):
    """
    Signup a new user
    :param request:
    :return:
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'users/user_signup.html', {'form': form})
