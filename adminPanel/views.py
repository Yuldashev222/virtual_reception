from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import Http404, HttpResponse
from django.shortcuts import redirect, render, get_object_or_404

from appeals.models import Answer, Appeal, Applicants_panel
from .forms import AddUserForm
from appeals.forms import ApplicantsPanelForm

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
    appeals = Appeal.objects.all().order_by('-created_date')

    context = {
        'appeals': appeals,
    }
            
    return render(request, 'adminPanel/appeals.html', context)


def answers(request):
    answers = Answer.objects.all().order_by('-created_date')

    context = {
        'answers': answers,
    }
            
    return render(request, 'adminPanel/answers.html', context)


def applicants_view(request):
    applicants_panel_info = Applicants_panel.objects.first()

    applicantsPanelForm = ApplicantsPanelForm(instance=applicants_panel_info)
    
    if request.POST:
        applicantsPanelForm = ApplicantsPanelForm(request.POST, request.FILES, instance=applicants_panel_info)
        
        if applicantsPanelForm.is_valid():
            obj = applicantsPanelForm.save(commit=False)
            obj.author = request.user
            obj.save()
            
            return redirect('applicants-view')
    
    context = {
        'applicantsPanelForm': applicantsPanelForm,
    }
    
            
    return render(request, 'adminPanel/applicants_panel.html', context)


def chat(request):
            
    return render(request, 'adminPanel/chat.html')


def profile(request, username):

    context = {

    }

    return render(request, 'adminPanel/profile.html', context)


def add_admin(request):
    addAdminForm = AddUserForm()
    
    if request.POST:
        addAdminForm = AddUserForm(request.POST)
        
        if addAdminForm.is_valid():
            admin = addAdminForm.save(commit=False)
            admin.save()
            
            return redirect('login')
            
    context = {
        'addAdminForm': addAdminForm,
    }

    return render(request, 'adminPanel/register.html', context)


def logout_admin(request, username):
    user = User.objects.get(username=username)
    
    logout(request)
    
    return redirect('login')

