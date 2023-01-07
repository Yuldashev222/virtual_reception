from django.http import JsonResponse

from django.shortcuts import render

from .forms import AppealForm
from .models import *


def post_appeal(request):
    appealForm = AppealForm(request.POST, request.FILES)
    if appealForm.is_valid():
        text = appealForm.cleaned_data["appeal_text"]
        file = appealForm.cleaned_data["appeal_file"]
        if text or file:
            obj = appealForm.save(commit=False)
            obj.save()
            new_appeals_cnt = Appeal.objects.filter(appeal_status="new").count()
            return JsonResponse({"applicant_name": obj.applicant_name, "applicant_email": obj.applicant_email, "appeal_code": obj.code, "new_appeals_cnt": new_appeals_cnt}, status=200)
        else:
            return JsonResponse({"errors": "hello guys"}, status=200)
    else:
        errors = appealForm.errors.as_json()
        return JsonResponse({"errors": errors}, status=400)


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
            answer['author'] = str(CustomUser.objects.get(id=answer['author_id']))
            answer['answer_type'] = Answer.objects.get(id=answer['id']).get_answer_type_display()
            answer['answer_address'] = Answer.objects.get(id=answer['id']).get_answer_address_display()
            answer['created_date'] = answer['created_date'].strftime('%Y-%m-%d || %H:%M')
            continue

        data['appeal_answers'] = appeal_answers
        data['appeal_answers_count'] = appeal_answers_count

        return JsonResponse(data)

    except:

        return JsonResponse(data)


def download_appealFile(request, id):
    try:
        appeal = Appeal.objects.get(id=request.GET['id'])
    except:
        appeal = Appeal.objects.get(id=id)
    filename = appeal.appeal_file.path
    response = FileResponse(open(filename, 'rb'))

    return response
