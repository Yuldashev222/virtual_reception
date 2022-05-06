import time
import json
from datetime import datetime, timedelta
from django.http import FileResponse, JsonResponse
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from django.http import FileResponse, Http404, HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.core.mail import send_mail

from appeals.models import Answer, Appeal, Applicants_panel
from .forms import AddUserForm, EditUserForm
from appeals.forms import AnswerForm, ApplicantsPanelForm

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
    new_appeals_cnt = Appeal.objects.filter(appeal_status='new').count()
    
    form = AnswerForm()
    appeals = Appeal.objects.all().order_by('-created_date')
    appeals_cnt = Appeal.objects.all().count()

    # search_appeal = request.GET.get('search')
    # search_date = request.GET.get('search_in_date')
    context = {
        'answer_form': form,
        'appeals': appeals,
        'appeals_cnt': appeals_cnt,
        'new_appeals_cnt': new_appeals_cnt,
        'today_date': datetime.today().strftime('%Y-%m-%d'),
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
                    appeals = appeals.filter( Q(appeal_status='done') | Q(appeal_status='rejected') )
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
                try:
                    valid_date = datetime.strptime(d['search_in_date'], '%Y-%m-%d')
                    # print(valid_date.tm_year, valid_date.tm_mon, valid_date.tm_mday)
                    
                    appeals = appeals.filter(Q(created_date__date=d['search_in_date']))
                except ValueError:
                    appeals = appeals.filter(created_date=str(datetime.today().date() + timedelta(days=1)))
                  
                    

            appeals = list(appeals.order_by('-created_date').values())

            for obj in appeals:
                obj['appeal_file'] = str(Appeal.objects.get(id=obj['id']).filename())
                continue
            

            data = {'appeals': appeals, 'appeals_cnt': len(appeals)}
            
            return JsonResponse(data)

        else:
            appeals = list(appeals.values())
            data = {'appeals': appeals, 'appeals_cnt': len(appeals)}
            return JsonResponse(data)


    return render(request, 'adminPanel/appeals.html', context)


def send_answer(request):
    form = AnswerForm(request.POST, request.FILES)

    answer = form.save(commit=False)
    appeal = Appeal.objects.get(id=answer.appeal.id)
    
    if answer.file or answer.text:
        
        # if answer.answer_address == 'email' or answer.answer_address == 'site_and_email':
        #     send_mail(
        #         subject='TDTrU', 
        #         message=answer.text, 
        #         from_email='oybekyuldashov54@gmail.com', 
        #         recipient_list=[appeal.applicant_email],
        #         fail_silently=False    
        #     )
            
            # if mail:
            #     answer.author = request.user 
            #     appeal.appeal_status = answer.answer_type
            #     appeal.save()
            #     answer.save() 

            #     return JsonResponse({'result': 'javob yuborildi'}, status=200)
                
            # else:
            #     return JsonResponse({'result': 'Emailga yuborishda xatolik'}, status=200)

        answer.author = request.user 
        appeal.appeal_status = answer.answer_type
        appeal.save()
        answer.save()
        
        appeal_answers = list(Answer.objects.filter(appeal=answer.appeal.id).values())
        for answer in appeal_answers:
            answer['author'] = str(User.objects.get(id=answer['author_id']))
            answer['answer_type'] = Answer.objects.get(id=answer['id']).get_answer_type_display()
            answer['answer_address'] = Answer.objects.get(id=answer['id']).get_answer_address_display()
            answer['created_date'] = answer['created_date'].strftime('%Y-%m-%d || %H:%M')
            continue

        return JsonResponse({
                                'result': 'javob yuborildi', 
                                'appeal_answers': appeal_answers, 
                                'appeal_status': appeal.get_appeal_status_display()
                            }, 
                            status=200)

    else:
        
        return JsonResponse(
                    {
                        'result': 'Javob yuborish uchun kamida text yoki file maydonlarini to\'ldiring', 
                        'appeal_answers': False
                    }, 
                    status=200
                )
            

def single_appeal(request, id):
    
    ajax_id = request.GET['id']
    
    new_appeals_cnt = Appeal.objects.filter(appeal_status='new').count()

    appeal = list(Appeal.objects.filter(id=ajax_id).values())
    
    
    appeal[0]['created_date'] = appeal[0]['created_date'].strftime('%d.%m.%Y || %H:%M')
    appeal[0]['appeal_file'] = str(Appeal.objects.get(id=appeal[0]['id']).filename())
    appeal[0]['applicant_province'] = str(Appeal.objects.get(id=appeal[0]['id']).get_applicant_province_display())
    appeal[0]['appeal_direction'] = str(Appeal.objects.get(id=appeal[0]['id']).get_appeal_direction_display())
    appeal[0]['appeal_type'] = str(Appeal.objects.get(id=appeal[0]['id']).get_appeal_type_display())
    appeal[0]['applicant_type'] = str(Appeal.objects.get(id=appeal[0]['id']).get_applicant_type_display())
    appeal[0]['applicant_position'] = str(Appeal.objects.get(id=appeal[0]['id']).get_applicant_position_display())
    appeal[0]['appeal_status'] = str(Appeal.objects.get(id=appeal[0]['id']).get_appeal_status_display())


    single_appeal = Appeal.objects.get(id=ajax_id)
    if single_appeal.appeal_status == 'new':
        single_appeal.appeal_status = single_appeal.APPEAL_STATUS[1][0]
        single_appeal.save()
    
    
    data = {'appeal': appeal[0], "appeal_answers": False, "appeal_answers_count": False, 'new_appeals_cnt': new_appeals_cnt}
    try:
        appeal_answers = list(Answer.objects.filter(appeal=request.GET['id']).values())
        appeal_answers_count = Answer.objects.filter(appeal=request.GET['id']).count()
        for answer in appeal_answers:
            answer['author'] = str(User.objects.get(id=answer['author_id']))
            answer['answer_type'] = Answer.objects.get(id=answer['id']).get_answer_type_display()
            answer['answer_address'] = Answer.objects.get(id=answer['id']).get_answer_address_display()
            answer['created_date'] = answer['created_date'].strftime('%Y-%m-%d || %H:%M')
            continue

        data['appeal_answers'] = appeal_answers
        data['appeal_answers_count'] = appeal_answers_count

        return JsonResponse(data)        

    except:

        return JsonResponse(data)        


def answers(request):
    new_appeals_cnt = Appeal.objects.filter(appeal_status='new').count()
    
    form = AnswerForm()
    answers = Answer.objects.all().order_by('-updated_date')
    answers_cnt = Answer.objects.all().count()

    # search_appeal = request.GET.get('search')
    # search_date = request.GET.get('search_in_date')
    context = {
        'answer_form': form,
        'answers': answers,
        'answers_cnt': answers_cnt,
        'new_appeals_cnt': new_appeals_cnt,
        'today_date': datetime.today().strftime('%Y-%m-%d'),
    }
    
    if request.GET:
        
        d = {}
        for key, val in request.GET.items():
            if val != 'all':
                d[key] = val
        
        if d:
            if 'applicant_province' in d:
                appeals = Appeal.objects.filter( Q(applicant_province=d['applicant_province']) )
                answers = Answer.objects.filter(appeal__in=appeals)
            
            # if 'appeal_direction' in d:
            #     appeals = appeals.filter( Q(appeal_direction=d['appeal_direction']) )
            
            # if 'appeal_type' in d:
            #     appeals = appeals.filter( Q(appeal_type=d['appeal_type']) )
            
            # if 'applicant_type' in d:
            #     appeals = appeals.filter( Q(applicant_type=d['applicant_type']) )
            
            # if 'appeal_status' in d:
            #     appeals = appeals.filter( Q(appeal_status=d['appeal_status']) )

            # if 'applicant_position' in d:
            #     appeals = appeals.filter( Q(applicant_position=d['applicant_position']) )
            
            # if 'yes_or_no_answer' in d:
            #     if d['yes_or_no_answer'] == 'yes':
            #         appeals = appeals.filter( Q(appeal_status='done') | Q(appeal_status='rejected') )
            #     else:
            #         appeals = appeals.filter( Q(appeal_status='new') | Q(appeal_status='process') )
            
            # if 'date' in d:
            #     if d['date'] == 'day':
            #         day = datetime.now() - timedelta(minutes=60*24)
            #         appeals = appeals.filter(created_date__gte=day)
                
            #     elif d['date'] == 'week':
            #         week = datetime.now() - timedelta(minutes=60*24*7)
            #         appeals = appeals.filter(created_date__gte=week)
                
            #     elif d['date'] == 'month':
            #         month = datetime.now() - timedelta(minutes=60*24*30)
            #         appeals = appeals.filter(created_date__gte=month)

            #     else:
            #         year = datetime.now() - timedelta(minutes=60*24*365)
            #         appeals = appeals.filter(created_date__gte=year)

            # if d['search']:
            #     appeals = appeals.filter(Q(applicant_name__icontains=d['search']))

            # if d['search_in_date']:
            #     try:
            #         valid_date = datetime.strptime(d['search_in_date'], '%Y-%m-%d')
            #         # print(valid_date.tm_year, valid_date.tm_mon, valid_date.tm_mday)
                    
            #         appeals = appeals.filter(Q(created_date__date=d['search_in_date']))
            #     except ValueError:
            #         appeals = appeals.filter(created_date=str(datetime.today().date() + timedelta(days=1)))
                  
                    

            # appeals = list(appeals.order_by('-created_date').values())
            answers = list(answers.order_by('-updated_date').values())

            for obj in appeals:
                obj['appeal_file'] = str(Appeal.objects.get(id=obj['id']).filename())
                continue
            

            data = {'answers': answers, 'answers_cnt': len(answers)}
            
            return JsonResponse(data)

        else:
            appeals = list(appeals.values())
            data = {'appeals': appeals, 'appeals_cnt': len(appeals)}
            return JsonResponse(data)


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
        'new_appeals_cnt': new_appeals_cnt,
        
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
    try: 
        appeal = Appeal.objects.get(id=request.GET['id'])
    except:
        appeal = Appeal.objects.get(id=id)
    filename = appeal.appeal_file.path
    response = FileResponse(open(filename, 'rb'))
    
    # if request.GET or True:
    #     appeal = Appeal.objects.get(id=request.GET['id'])
    #     filename = appeal.appeal_file.path
    #     response = FileResponse(open(filename, 'rb'))
        
    
    return response


def download_answerFile(request, id):
    answer = Answer.objects.get(id=id)
    filename = answer.file.path
    response = FileResponse(open(filename, 'rb'))
    return response


# def test(request):
#     if request.method == 'POST':
#         send_mail('hello', 'test message', 'oybekyuldashov54@gmail.com', ['oybekyuldashov54@gmail.com'])
        
#     return render(request, 'test.html')