from django.http import JsonResponse
from django.db.models import Count, Q
from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404

from appeals.forms import AppealForm
from appeals.models import Appeal
from answers.models import Answer
from .models import ApplicantsTemplate, EduSocial
from .forms import ApplicantsPanelForm

from accounts.models import CustomUser
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
    socials = EduSocial.objects.all()[:4]

    appeal_form = AppealForm()

    context = {
        'appeal_form': appeal_form,
        'applicants_panel_info': applicants_panel_info,
        'socials': socials,

        # STATISTICS
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


def dashboard(request, username):
    user = get_object_or_404(CustomUser, username=username)

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
    for user in CustomUser.objects.all():
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
