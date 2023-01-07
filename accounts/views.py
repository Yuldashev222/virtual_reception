import time
import json
from datetime import datetime, timedelta

from django.http import FileResponse, JsonResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render

from appeals.models import Appeal
from .forms import AddUserForm, EditUserForm

# app imports
from .models import CustomUser


def admin_login(request):
    if request.user.is_authenticated:
        return redirect('dashboard', request.user.username)

    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)

            return redirect('dashboard', user.username)

        else:
            messages.error(request, "Login yoki parol noto'g'ri")

            return redirect('login')

    return render(request, 'adminPanel/login.html')


def profile(request, username):
    user = CustomUser.objects.get(username=username)
    new_appeals_cnt = Appeal.objects.filter(appeal_status='new').count()

    edit_user = EditUserForm(instance=user, use_required_attribute=False)

    if request.POST:
        edit_user = EditUserForm(request.POST or None, request.FILES or None, instance=user,
                                 use_required_attribute=False)

        if edit_user.is_valid():
            edit_user.save()

            return redirect('profile', user.username)

    context = {
        'new_appeals_cnt': new_appeals_cnt,
        'user': user,
        'edit_user': edit_user,

    }

    return render(request, 'adminPanel/profile.html', context)


def add_admin(request):
    new_appeals_cnt = Appeal.objects.filter(appeal_status='new').count()

    addAdminForm = AddUserForm()

    if request.POST:
        addAdminForm = AddUserForm(request.POST)

        if addAdminForm.is_valid():
            admin = addAdminForm.save(commit=False)
            admin.save()

            return redirect('login')

    context = {
        'addAdminForm': addAdminForm,
        'new_appeals_cnt': new_appeals_cnt,

    }

    return render(request, 'adminPanel/register.html', context)


def logout_admin(request, username):
    user = User.objects.get(username=username)

    logout(request)

    return redirect('login')
