from django.http import JsonResponse
from django.db.models import Count, Q
from django.shortcuts import redirect, render

from appeals.forms import AppealForm
from appeals.models import Appeal
from answers.models import Answer
from .models import ApplicantsTemplate, EduSocial
from .forms import ApplicantsPanelForm

from appeals.enums import AppealStatus


def home(request):
    # STATISTICS
    appeal_count_by_status = Appeal.objects.aggregate(
        process_appeals_cnt=Count('appeal_status', filter=Q(appeal_status=AppealStatus.p.name)),
        rejected_appeals_cnt=Count('appeal_status', filter=Q(appeal_status=AppealStatus.r.name)),
        completed_appeals_cnt=Count('appeal_status', filter=Q(appeal_status=AppealStatus.d.name)),
        new_appeals_cnt=Count('appeal_status', filter=Q(appeal_status=AppealStatus.n.name))
    )

    applicants_panel_info = ApplicantsTemplate.objects.first()
    socials = EduSocial.objects.all()

    appeal_form = AppealForm()

    context = {
        'appeal_form': appeal_form,
        'applicants_panel_info': applicants_panel_info,
        'socials': socials,

        'all_appeals_cnt': sum(appeal_count_by_status.values()),
        'appeal_count_by_status': appeal_count_by_status,
    }

    code = request.GET.get('appeal_code')
    if code:
        try:
            appeal = Appeal.objects.get(code=str(code))
            try:
                answers = Answer.objects.filter(appeal_id=appeal.id).order_by("updated_date")

                message = f"{appeal.applicant_name} javobi:"
                appeal_date = str(appeal.created_date.strftime("%d.%m.%Y || %H:%M"))
                last_answer_date = Answer.objects.filter(appeal_id=appeal.id).order_by(
                    "-updated_date").first().updated_date_format()
                last_answer_type = Answer.objects.filter(appeal_id=appeal.id).order_by(
                    "-updated_date").first().get_answer_type_display()
                return JsonResponse({'answers': answers, "last_answer_type": last_answer_type, 'message': message,
                                     "last_answer_date": last_answer_date, "appeal_date": appeal_date}, status=200)

            except:
                message = "{}. Sizning murojaatingiz ko'rib chiqilmoqda".format(appeal.applicant_name)
                response = JsonResponse({"error": message})
                response.status_code = 403
                return response

        except Appeal.DoesNotExist:
            message = "Xato id kiritdingiz..."
            response = JsonResponse({"error": message})
            response.status_code = 403
            return response  # last
    return render(request, 'index.html', context)


def applicants_view(request):
    new_appeals_cnt = Appeal.objects.filter(appeal_status='new').count()

    applicants_panel_info = ApplicantsTemplate.objects.first()

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
