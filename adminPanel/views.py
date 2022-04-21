import json
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

appeals_cnt = Appeal.objects.filter(appeal_status='new').count()


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
        'appeals_cnt': appeals_cnt,
        
    }
            
    return render(request, 'adminPanel/dashboard.html', context)



def filter_appeals_or_all_appeals(request):
    appeals = Appeal.objects.all()
    
    # Filter objs
    appeal_type = request.GET.get('appeal_type')
    province = request.GET.get('province')
    appeal_direction = request.GET.get('appeal_direction')
    applicant_type = request.GET.get('applicant_type')
    appeal_status = request.GET.get('appeal_status')
    applicant_position = request.GET.get('applicant_position')

    yes_or_no_answer = request.GET.get('yes_or_no_answer')
    date = request.GET.get('date')
    
    
    if province or appeal_direction or appeal_type or applicant_type or appeal_status or applicant_position or yes_or_no_answer:
        
        appeals = appeals.filter(
              Q(applicant_province=province)
            | Q(appeal_direction=appeal_direction)
            | Q(appeal_type=appeal_type)
            | Q(applicant_type=applicant_type)
            | Q(appeal_status=appeal_status)
            | Q(applicant_position=applicant_position)
            )


        test = False
        if not appeals:
            appeals = Appeal.objects.all()
            test = True

        if yes_or_no_answer == 'yes':
            appeals = appeals.filter( Q(appeal_status="rejected") | Q(appeal_status="completed") )

        elif yes_or_no_answer == 'on':
            appeals = appeals.filter( Q(appeal_status='new') | Q(appeal_status='process') )


        if test:
            messages.error(request, 'Filter bo\'yicha murojaat kelmagan')
            appeals = Appeal.objects.all()


    return appeals


def appeals(request):
    appeals = filter_appeals_or_all_appeals(request).order_by('-created_date')

    search_appeal = request.GET.get('search')
    search_date = request.GET.get('search_in_date')
    
    context = {
        'appeals': appeals,
        'appeals_cnt': appeals_cnt,
    }
    is_ajax = request.GET.get('optionValue')
    
    if is_ajax:
        if request.method == 'GET':
            country = request.GET.get('optionValue')
            if country:
                appeals = Appeal.objects.filter(applicant_province=country).values()
                if appeals:
                    data ={'appeals':list(appeals)}
                    return JsonResponse(data)
                else:
                    messages.error(request, 'sadasdasdasd')
                    data ={'appeals':list(appeals)}
                    return JsonResponse(data)
            else:
                appeals = Appeal.objects.all().values()
                
                
        
        
    if search_appeal:
        appeals = Appeal.objects.filter(Q(applicant_name__icontains=search_appeal)).order_by('-created_date')

        if not appeals:
            
            messages.error(request, "Murojaat topilmadi")
            return redirect('appeals')
        
        else:
            context['appeals'] = appeals
            context['search_appeal'] = search_appeal
            messages.success(request, f'{appeals.count()} ta Murojaat topildi')
    
    
    elif search_date:
        try:
            appeals = Appeal.objects.filter(created_date__date=search_date)
        except:
            return redirect('appeals')
        

        if appeals:
            context['appeals'] = appeals
            messages.success(request, f"{search_date} sana bo'yicha {appeals.count()} ta Murojaat topildi")        

        else:
            context['search_date'] = search_date
            messages.error(request, 'Murojaat topilmadi')
            return redirect('appeals')


    return render(request, 'adminPanel/appeals.html', context)


def answers(request):
    answers = Answer.objects.all().order_by('-created_date')

    context = {
        'answers': answers,
        'appeals_cnt': appeals_cnt,
        
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
        'appeals_cnt': appeals_cnt,
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
        'appeals_cnt': appeals_cnt,
        
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
    

    