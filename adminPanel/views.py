import time
import json
from datetime import datetime, timedelta

import pandas
from django.http import FileResponse, JsonResponse
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from django.http import FileResponse, Http404, HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.core.mail import send_mail
from django.utils import timezone

from appeals.models import Answer, Appeal, Applicants_panel
from django.conf import settings
from config.settings import EMAIL_HOST, EMAIL_HOST_USER
from .forms import AddUserForm, EditUserForm
from appeals.forms import AnswerForm, ApplicantsPanelForm

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

            return redirect('login')

    return render(request, 'adminPanel/login.html')


def dashboard(request, username):
    user = get_object_or_404(User, username=username)

    if request.user.username != user.username:
        return HttpResponse('Error')

    new_appeals_cnt = Appeal.objects.filter(appeal_status='new').count()

    # APPEAL STATUSES
    appeal_status = {}
    for status in Appeal.APPEAL_STATUS:
        appeal_status[status[0]] = Appeal.get_cnt_status(status[0])

    # APPEAL DIRECTION
    appeal_direction = {}
    for direction in Appeal.APPEAL_DIRECTION:
        appeal_direction[direction[0]] = Appeal.get_cnt_direction(direction[0])

    # APPEAL TYPES
    appeal_type = {}
    for type in Appeal.APPEAL_TYPE:
        appeal_type[type[0]] = Appeal.get_cnt_type(type[0])

    # ANSWER AUTHOR
    admins = {}
    for user in User.objects.all():
        admins[user.username] = Answer.get_cnt_appeals_admin(user)

    # APPLICANT TYPES
    applicant_type = {}
    for type in Appeal.APPLICANT_TYPE:
        applicant_type[type[0]] = Appeal.get_cnt_applicant_type(type[0])

    # APPLICANT POSITION
    applicant_position = {}
    for position in Appeal.APPLICANT_POSITION:
        applicant_position[position[0]] = Appeal.get_cnt_applicant_position(position[0])

    # APPEAL COUNTRIES
    appeal_country = {}
    for country in Appeal.PROVINCE:
        appeal_country[country[0]] = Appeal.get_cnt_country(country[0])

    # APPEAL ADDRESSES
    answer_address = {}
    for address in Answer.ANSWER_ADDRESS:
        answer_address[address[0]] = Answer.get_cnt_answer_address(address[0])

    context = {
        'new_appeals_cnt': new_appeals_cnt,

        # APPEAL TYPE
        'appeal_type': Appeal.APPEAL_TYPE,
        'appeal_type_cnt': list(appeal_type.values()),

        # ANSWER AUTHOR
        'admin_names': list(admins.keys()),
        'admin_cnt': list(admins.values()),

        # APPLICANT TYPE
        'applicant_type': Appeal.APPLICANT_TYPE,
        'applicant_type_cnt': list(applicant_type.values()),

        # APPLICANT POSITION
        'applicant_position': Appeal.APPLICANT_POSITION,
        'applicant_position_cnt': list(applicant_position.values()),

        # APPEAL STATUS
        'appeal_status': Appeal.APPEAL_STATUS,
        'appeal_status_cnt': list(appeal_status.values()),

        # APPEAL DIRECTION
        'appeal_direction': Appeal.APPEAL_DIRECTION,
        'appeal_direction_cnt': list(appeal_direction.values()),

        # ANSWER ADDRESSES
        'answer_address': Answer.ANSWER_ADDRESS,
        'answer_address_cnt': list(answer_address.values()),

        # APPEAL COUNTRIES
        'appeal_country': list(appeal_country.values()),
    }

    return render(request, 'adminPanel/dashboard.html', context)


def appeals(request):
    new_appeals_cnt = Appeal.objects.filter(appeal_status='new').count()
    form = AnswerForm()
    appeals = Appeal.objects.all().order_by('-created_date')
    appeals_cnt = Appeal.objects.all().count()
    # print(list(map(lambda elem: elem["created_date"].day, appeals.values("created_date"))))
    # print()
    # print()
    # print()
    # print()
    # print()
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
                appeals = Appeal.objects.filter(Q(applicant_province=d['applicant_province']))

            if 'appeal_direction' in d:
                appeals = appeals.filter(Q(appeal_direction=d['appeal_direction']))

            if 'appeal_type' in d:
                appeals = appeals.filter(Q(appeal_type=d['appeal_type']))

            if 'applicant_type' in d:
                appeals = appeals.filter(Q(applicant_type=d['applicant_type']))

            if 'appeal_status' in d:
                appeals = appeals.filter(Q(appeal_status=d['appeal_status']))

            if 'applicant_position' in d:
                appeals = appeals.filter(Q(applicant_position=d['applicant_position']))

            if 'yes_or_no_answer' in d:
                if d['yes_or_no_answer'] == 'yes':
                    appeals = appeals.filter(Q(appeal_status='done') | Q(appeal_status='rejected'))
                else:
                    appeals = appeals.filter(Q(appeal_status='new') | Q(appeal_status='process'))

            if 'date' in d:
                if d['date'] == 'day':
                    day = datetime.now() - timedelta(minutes=60 * 24)
                    appeals = appeals.filter(created_date__gte=day, created_date__lte=datetime.now())

                elif d['date'] == 'week':
                    week = datetime.now() - timedelta(minutes=60 * 24 * 7)
                    appeals = appeals.filter(created_date__gte=week, created_date__lte=datetime.now())

                elif d['date'] == 'month':
                    month = datetime.now() - timedelta(minutes=60 * 24 * 30)
                    appeals = appeals.filter(created_date__gte=month, created_date__lte=datetime.now())

                else:
                    year = datetime.now() - timedelta(minutes=60 * 24 * 365)
                    appeals = appeals.filter(created_date__gte=year, created_date__lte=datetime.now())

            if d['search']:
                appeals = appeals.filter(
                    Q(applicant_name__icontains=d['search']) |
                    Q(appeal_subject__icontains=d['search']) |
                    Q(appeal_text__icontains=d['search'])
                )

            if d['search_in_date']:
                try:
                    valid_date = datetime.strptime(d['search_in_date'], '%Y-%m-%d')

                    appeals = appeals.filter(Q(created_date__date=d['search_in_date']))
                except ValueError:
                    appeals = appeals.filter(created_date=str(datetime.today().date() + timedelta(days=1)))

        appeals = list(appeals.order_by('-created_date').values())

        for obj in appeals:
            obj['appeal_file'] = str(Appeal.objects.get(id=obj['id']).filename())

            if obj["created_date"] + timedelta(days=1) + timedelta(minutes=60 * 24 * 3) <= timezone.now():
                obj["set_date"] = 3
            elif obj["created_date"] + timedelta(days=1) + timedelta(minutes=60 * 24 * 2) <= timezone.now():
                obj["set_date"] = 2
            elif obj["created_date"] + timedelta(days=1) + timedelta(minutes=60 * 24) <= timezone.now():
                obj["set_date"] = 1
            else:
                obj["set_date"] = 0

        data = {'appeals': appeals, 'appeals_cnt': len(appeals)}

        return JsonResponse(data)

    return render(request, 'adminPanel/appeals.html', context)


def single_appeal(request):
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

    data = {'appeal': appeal[0], "appeal_answers": False, "appeal_answers_count": False,
            'new_appeals_cnt': new_appeals_cnt}
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


def send_answer(request):
    form = AnswerForm(request.POST, request.FILES)
    answer = form.save(commit=False)
    appeal = Appeal.objects.get(id=answer.appeal.id)

    if answer.file or answer.text:

        answer.author = request.user
        appeal.appeal_status = answer.answer_type
        appeal.save()
        answer.save()
        # subject = "TSTU: murojaat javobi"
        # message = answer.text
        # my_email = settings.EMAIL_HOST_USER
        # recepient_email = answer.appeal.applicant_email
        # recepient_email = "test2@maxsoft.uz"
        # send_mail(subject=subject, message=message, from_email=my_email, recipient_list=[recepient_email], fail_silently=False)

        appeal_answers = list(Answer.objects.filter(appeal=answer.appeal.id).values())
        for answer in appeal_answers:
            answer['author'] = str(User.objects.get(id=answer['author_id']))
            answer['answer_type'] = Answer.objects.get(id=answer['id']).get_answer_type_display()
            answer['answer_address'] = Answer.objects.get(id=answer['id']).get_answer_address_display()
            answer['created_date'] = answer['created_date'].strftime('%Y-%m-%d || %H:%M')

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
                'appeal_answers': False,
                'appeal_status': appeal.get_appeal_status_display(),

            },
            status=200
        )


def answers(request):
    new_appeals_cnt = Appeal.objects.filter(appeal_status='new').count()

    new_appeals_cnt = Appeal.objects.filter(appeal_status='new').count()

    form = AnswerForm()
    answers = Answer.objects.all().order_by('-updated_date')
    appeals = Appeal.objects.all()
    answers_cnt = Answer.objects.all().count()

    admins = User.objects.exclude(username=request.user.username)

    context = {
        'answer_form': form,
        'admins': admins,
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
                appeals = Appeal.objects.filter(Q(applicant_province=d['applicant_province']))
                answers = Answer.objects.filter(appeal__in=appeals)

            if 'appeal_direction' in d:
                appeals = appeals.filter(Q(appeal_direction=d['appeal_direction']))
                answers = answers.filter(appeal__in=appeals)

            if 'appeal_type' in d:
                appeals = appeals.filter(Q(appeal_type=d['appeal_type']))
                answers = answers.filter(appeal__in=appeals)

            if 'answer_type' in d:
                answers = answers.filter(answer_type=d['answer_type'])

            if 'answer_address' in d:
                answers = answers.filter(answer_address=d['answer_address'])

            if 'active' in d:
                answers = answers.filter(active=d['active'])

            if 'author' in d:
                answers = answers.filter(author_id=d['author'])

            if 'date' in d:
                if d['date'] == 'day':
                    day = datetime.now() - timedelta(minutes=60 * 24)
                    answers = answers.filter(updated_date__gte=day, updated_date__lte=datetime.now())

                elif d['date'] == 'week':
                    week = datetime.now() - timedelta(minutes=60 * 24 * 7)
                    answers = answers.filter(updated_date__gte=week, updated_date__lte=datetime.now())

                elif d['date'] == 'month':
                    month = datetime.now() - timedelta(minutes=60 * 24 * 30)
                    answers = answers.filter(updated_date__gte=month, updated_date__lte=datetime.now())

                else:
                    year = datetime.now() - timedelta(minutes=60 * 24 * 365)
                    answers = answers.filter(updated_date__gte=year, updated_date__lte=datetime.now())

            if d['search']:
                appeals = Appeal.objects.filter(applicant_name__icontains=d['search'])
                answers = answers.filter(Q(appeal__in=appeals) | Q(text__icontains=d['search']))

            if d['search_in_date']:
                try:
                    valid_date = datetime.strptime(d['search_in_date'], '%Y-%m-%d')

                    answers = answers.filter(
                        Q(created_date__date=d['search_in_date']) | Q(updated_date__date=d['search_in_date']))

                except ValueError:
                    pass

        answers = list(answers.order_by('-updated_date').values())

        for obj in answers:
            obj['author'] = str(User.objects.get(id=obj['author_id']))
            obj['updated_date'] = obj['updated_date'].strftime('%d-%m-%Y || %H:%M')

            if obj['appeal_id']:
                obj['appeal'] = str(Appeal.objects.get(id=obj['appeal_id']))
            else:
                obj['appeal'] = 'O\'chirilgan'

            if obj['answer_type'] == 'done':
                obj['answer_type'] = 'Bajarilgan'
            else:
                obj['answer_type'] = 'Rad etilgan'

            if obj['file']:
                obj['file'] = str(Answer.objects.get(id=obj['id']).filename())
            else:
                obj['file'] = '-'

        data = {'answers': answers, 'answers_cnt': len(answers)}

        return JsonResponse(data)

    return render(request, 'adminPanel/answers.html', context)


def single_answer(request):
    ajax_id = request.GET['id']

    answer = list(Answer.objects.filter(id=ajax_id).values())

    answer[0]['updated_date'] = answer[0]['updated_date'].strftime('%d.%m.%Y || %H:%M')
    answer[0]['created_date'] = answer[0]['created_date'].strftime('%d.%m.%Y || %H:%M')
    answer[0]['file'] = str(Answer.objects.get(id=answer[0]['id']).filename())
    answer[0]['answer_type'] = str(Answer.objects.get(id=answer[0]['id']).get_answer_type_display())
    answer[0]['answer_address'] = str(Answer.objects.get(id=answer[0]['id']).get_answer_address_display())
    answer[0]['active_display'] = str(Answer.objects.get(id=answer[0]['id']).get_active_display())
    answer[0]['author'] = str(User.objects.get(id=answer[0]['author_id']).username)

    try:
        answer[0]['appeal'] = str(Appeal.objects.get(id=answer[0]['appeal_id']).applicant_name)
    except:
        answer[0]['appeal'] = 'O\'chirilgan'

    # single_appeal = Appeal.objects.get(id=ajax_id)
    # if single_appeal.appeal_status == 'new':
    #     single_appeal.appeal_status = single_appeal.APPEAL_STATUS[1][0]
    #     single_appeal.save()

    data = {'answer': answer[0]}

    return JsonResponse(data)


def edit_answer(request):
    if request.GET:
        id = request.GET['answer_id']
        answer = list(Answer.objects.filter(id=id).values())
        appeal = Appeal.objects.get(id=answer[0]['appeal_id'])

        if appeal.applicant_email:
            answer[0]['appeal_email'] = appeal.applicant_email
        else:
            answer[0]['appeal_email'] = False

        answer[0]['updated_date'] = answer[0]['updated_date'].strftime('%d.%m.%Y || %H:%M')
        answer[0]['created_date'] = answer[0]['created_date'].strftime('%d.%m.%Y || %H:%M')
        answer[0]['file'] = str(Answer.objects.get(id=answer[0]['id']).filename())
        answer[0]['answer_type_display'] = str(Answer.objects.get(id=answer[0]['id']).get_answer_type_display())
        answer[0]['answer_address_display'] = str(Answer.objects.get(id=answer[0]['id']).get_answer_address_display())
        answer[0]['active_display'] = str(Answer.objects.get(id=answer[0]['id']).get_active_display())
        answer[0]['author'] = str(User.objects.get(id=answer[0]['author_id']).username)

        answer[0]['appeal'] = str(Appeal.objects.get(id=answer[0]['appeal_id']).applicant_name)

        return JsonResponse({'answer': answer[0]})

    else:
        answer = Answer.objects.get(id=request.POST['id'])
        appeal = Appeal.objects.get(id=answer.appeal.id)

        if request.POST['text']:  # ***********************

            answer.answer_address = request.POST['answer_address']
            answer.active = request.POST['active']
            answer.answer_type = request.POST['answer_type']
            answer.text = request.POST['text']
            answer.author = request.user
            appeal.appeal_status = answer.answer_type

            appeal.save()
            answer.save()

            edit_none = False
            if answer.active == 'send':
                edit_none = True

            return JsonResponse(
                {
                    'result': 'javob muvafaqqiyatli o\'zgartirildi',
                    'appeal_status': appeal.get_appeal_status_display(),
                    'answer_id': answer.id,
                    'edit_none': edit_none,
                },
                status=200
            )

        else:

            return JsonResponse(
                {'result': 'Javob yuborish uchun kamida text yoki file maydonlarini to\'ldiring'}, status=200
            )


def delete_answer(request):
    answer_id = request.GET['id']
    answer = Answer.objects.get(id=answer_id)
    answer.delete()

    return JsonResponse({})


def applicants_view(request):
    new_appeals_cnt = Appeal.objects.filter(appeal_status='new').count()

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


def download_appealFile(request, id):
    try:
        appeal = Appeal.objects.get(id=request.GET['id'])
    except:
        appeal = Appeal.objects.get(id=id)
    filename = appeal.appeal_file.path
    response = FileResponse(open(filename, 'rb'))

    return response


def download_answerFile(request, id):
    try:
        answer = Answer.objects.get(id=request.GET['id'])
    except:
        answer = Answer.objects.get(id=id)
    filename = answer.file.path
    response = FileResponse(open(filename, 'rb'))

    return response
