from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import Http404, HttpResponse
from django.shortcuts import redirect, render, get_object_or_404

# app imports
from .models import User


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
                
    return render(request, 'adminPanel/login.html')


def dashboard(request, username):
    user = get_object_or_404(User, username=username)

    if request.user.username != user.username:
        return HttpResponse('Error')
            
    return render(request, 'adminPanel/dashboard.html')


def appeals(request):
            
    return render(request, 'adminPanel/appeals.html')


def answers(request):
            
    return render(request, 'adminPanel/answers.html')


def applicants_view(request):
            
    return render(request, 'adminPanel/applicants_panel.html')


def chat(request):
            
    return render(request, 'adminPanel/chat.html')
