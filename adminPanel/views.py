import json
from datetime import datetime, timedelta
from django.http import FileResponse, JsonResponse
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from django.http import FileResponse, Http404, HttpResponse
from django.shortcuts import redirect, render, get_object_or_404

from appeals.models import Answer, Appeal, Applicants_panel
from .forms import AddUserForm, EditUserForm
from appeals.forms import ApplicantsPanelForm

# app imports
from .models import User

new_appeals_cnt = Appeal.objects.filter(appeal_status='new').count()


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


def dashboard(request, username):
    user = get_object_or_404(User, username=username)

    if request.user.username != user.username:
        return HttpResponse('Error')

    context = {
        'new_appeals_cnt': new_appeals_cnt,
        
    }
            
    return render(request, 'adminPanel/dashboard.html', context)


def appeals(request):
    appeals = Appeal.objects.all().order_by('-created_date')
    new_appeals_cnt = Appeal.objects.all().count()

    # search_appeal = request.GET.get('search')
    # search_date = request.GET.get('search_in_date')
    context = {
        'appeals': appeals,
        'new_appeals_cnt': new_appeals_cnt,
    }
    
    if request.GET:
        
        d = {}
        for key, val in request.GET.items():
            if val != 'all':
                d[key] = val
        
        if d:
            if 'applicant_province' in d:
                appeals = Appeal.objects.filter( Q(applicant_province=d['applicant_province']) )
            
            if 'appeal_direction' in d:
                appeals = appeals.filter( Q(appeal_direction=d['appeal_direction']) )
            
            if 'appeal_type' in d:
                appeals = appeals.filter( Q(appeal_type=d['appeal_type']) )
            
            if 'applicant_type' in d:
                appeals = appeals.filter( Q(applicant_type=d['applicant_type']) )
            
            if 'appeal_status' in d:
                appeals = appeals.filter( Q(appeal_status=d['appeal_status']) )

            if 'applicant_position' in d:
                appeals = appeals.filter( Q(applicant_position=d['applicant_position']) )
            
            if 'yes_or_no_answer' in d:
                if d['yes_or_no_answer'] == 'yes':
                    appeals = appeals.filter( Q(appeal_status='completed') | Q(appeal_status='rejected') )
                else:
                    appeals = appeals.filter( Q(appeal_status='new') | Q(appeal_status='process') )
            
            if 'date' in d:
                
                if d['date'] == 'day':
                    day = datetime.now() - timedelta(minutes=60*24)
                    appeals = appeals.filter(created_date__gte=day)
                
                elif d['date'] == 'week':
                    week = datetime.now() - timedelta(minutes=60*24*7)
                    appeals = appeals.filter(created_date__gte=week)
                
                elif d['date'] == 'month':
                    month = datetime.now() - timedelta(minutes=60*24*30)
                    appeals = appeals.filter(created_date__gte=month)

                else:
                    year = datetime.now() - timedelta(minutes=60*24*365)
                    appeals = appeals.filter(created_date__gte=year)

            if d['search']:
                appeals = appeals.filter(Q(applicant_name__icontains=d['search']))
            
            if d['search_in_date']:
                appeals = appeals.filter(Q(created_date__date=d['search_in_date']))
                print(appeals, '//////////')
                
            
            appeals = list(appeals.order_by('-created_date').values())
            data = {'appeals': appeals, 'appeals_cnt': len(appeals)}
            
            return JsonResponse(data)

        else:
            appeals = list(appeals.values())
            data = {'appeals': appeals, 'appeals_cnt': len(appeals)}
            print('-----------------')
            return JsonResponse(data)
            
                
    return render(request, 'adminPanel/appeals.html', context)
        
    # if search_appeal:
        
    #     appeals = Appeal.objects.filter(Q(applicant_name__icontains=search_appeal)).order_by('-created_date')

    #     if not appeals:
            
    #         messages.error(request, "Murojaat topilmadi")
    #         return redirect('appeals')
        
    #     else:
    #         context['appeals'] = appeals
    #         context['search_appeal'] = search_appeal
    #         messages.success(request, f'{appeals.count()} ta Murojaat topildi')
    
    
    # elif search_date:
        
    #     try:
    #         appeals = Appeal.objects.filter(created_date__date=search_date)
    #     except:
    #         return redirect('appeals')
        

    #     if appeals:
    #         context['appeals'] = appeals
    #         messages.success(request, f"{search_date} sana bo'yicha {appeals.count()} ta Murojaat topildi")        

    #     else:
    #         context['search_date'] = search_date
    #         messages.error(request, 'Murojaat topilmadi')
    #         return redirect('appeals')




def answers(request):
    answers = Answer.objects.all().order_by('-created_date')

    context = {
        'answers': answers,
        'new_appeals_cnt': new_appeals_cnt,
        
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
        'appeals_cnt': appeals_cnt,
        
    }
    
            
    return render(request, 'adminPanel/applicants_panel.html', context)


def chat(request):
            
    return render(request, 'adminPanel/chat.html')


def profile(request, username):
    user = User.objects.get(username=username)
    
    edit_user = EditUserForm(instance=user, use_required_attribute=False)
    
    if request.POST:
        edit_user = EditUserForm(request.POST or None, request.FILES or None, instance=user, use_required_attribute=False)
        
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


def download_appealFile(request, id):
    appeal = Appeal.objects.get(id=id)
    filename = appeal.appeal_file.path
    response = FileResponse(open(filename, 'rb'))
    return response


def download_answerFile(request, id):
    answer = Answer.objects.get(id=id)
    filename = answer.file.path
    response = FileResponse(open(filename, 'rb'))
    return response
    

    