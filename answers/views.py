from django.shortcuts import render

# Create your views here.


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
            answer['author'] = str(CustomUser.objects.get(id=answer['author_id']))
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

    admins = CustomUser.objects.exclude(username=request.user.username)

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
            obj['author'] = str(CustomUser.objects.get(id=obj['author_id']))
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
    answer[0]['author'] = str(CustomUser.objects.get(id=answer[0]['author_id']).username)

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
        answer[0]['author'] = str(CustomUser.objects.get(id=answer[0]['author_id']).username)

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


def download_answerFile(request, id):
    try:
        answer = Answer.objects.get(id=request.GET['id'])
    except:
        answer = Answer.objects.get(id=id)
    filename = answer.file.path
    response = FileResponse(open(filename, 'rb'))

    return response
