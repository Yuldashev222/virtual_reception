from django.core.mail import send_mail
from django.http import JsonResponse

from django.shortcuts import redirect, render
from django.contrib import messages

from .forms import AppealForm
from .models import *


def home(request):
    # STATISTICS
    all_appeals_cnt = Appeal.objects.all().count()
    process_appeals_cnt = Appeal.objects.filter(appeal_status='process').count()
    rejected_appeals_cnt = Appeal.objects.filter(appeal_status='rejected').count()
    completed_appeals_cnt = Appeal.objects.filter(appeal_status='done').count()
    new_appeals_cnt = Appeal.objects.filter(appeal_status='new').count()

    applicants_panel_info = Applicants_panel.objects.first()
    socials = Social.objects.all()
    appealForm = AppealForm()

    context = {
        'appealForm': appealForm,
        'applicants_panel_info': applicants_panel_info,
        'socials': socials,

        # STATISTICS
        'all_appeals_cnt': all_appeals_cnt,
        'process_appeals_cnt': process_appeals_cnt,
        'rejected_appeals_cnt': rejected_appeals_cnt,
        'completed_appeals_cnt': completed_appeals_cnt,
        'new_appeals_cnt': new_appeals_cnt,
    }

    if request.GET:
        code = request.GET['appeal_code']
        try:
            appeal = Appeal.objects.get(code=code)
            try:
                answers = list(Answer.objects.filter(appeal_id=appeal.id).order_by("updated_date").values())
                for answer in answers:
                    answer['updated_date_format'] = str(Answer.objects.get(id=answer["id"]).updated_date_format())
                    answer['answer_type_display'] = str(Answer.objects.get(id=answer["id"]).get_answer_type_display())
                    answer['file'] = str(Answer.objects.get(id=answer["id"]).filename())

                message = f"{appeal.applicant_name} javobi:"
                appeal_date = str(appeal.created_date.strftime("%d.%m.%Y || %H:%M"))
                last_answer_date = Answer.objects.filter(appeal_id=appeal.id).order_by("-updated_date").first().updated_date_format()
                last_answer_type = Answer.objects.filter(appeal_id=appeal.id).order_by("-updated_date").first().get_answer_type_display()
                return JsonResponse({'answers': answers, "last_answer_type": last_answer_type, 'message': message, "last_answer_date": last_answer_date, "appeal_date": appeal_date}, status=200)

            except:
                message = "{}. Sizning murojaatingiz ko'rib chiqilmoqda".format(appeal.applicant_name)
                response = JsonResponse({"error": message})
                response.status_code = 403
                return response

        except:
            message = "Xato id kiritdingiz..."
            response = JsonResponse({"error": message})
            response.status_code = 403
            return response

    return render(request, 'index.html', context)


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


