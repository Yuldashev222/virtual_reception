from django.contrib import messages
from django.db.models import Count, Q
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from answers.enums import AnswerAddress
from answers.models import Answer
from appeals.enums import AppealStatus, AppealType, ApplicantType, ApplicantPosition, Provinces
from appeals.models import Appeal, AppealDirection
from .forms import AddUserForm, EditUserForm
from .models import CustomUser


@login_required
def dashboard(request):
    # new_appeals_cnt = Appeal.objects.filter(appeal_status='new').count()

    appeal_cnt_by_choices = Appeal.objects.aggregate(
        process_appeals_cnt=Count('appeal_status', filter=Q(appeal_status=AppealStatus.p.name)),
        rejected_appeals_cnt=Count('appeal_status', filter=Q(appeal_status=AppealStatus.r.name)),
        completed_appeals_cnt=Count('appeal_status', filter=Q(appeal_status=AppealStatus.d.name)),
        new_appeals_cnt=Count('appeal_status', filter=Q(appeal_status=AppealStatus.n.name)),

        a_appeals_cnt=Count('appeal_type', filter=Q(appeal_type=AppealType.a.name)),
        s_appeals_cnt=Count('appeal_type', filter=Q(appeal_type=AppealType.s.name)),
        t_appeals_cnt=Count('appeal_type', filter=Q(appeal_type=AppealType.t.name)),
        b_appeals_cnt=Count('appeal_type', filter=Q(appeal_type=AppealType.b.name)),

        y_appeals_cnt=Count('applicant_type', filter=Q(applicant_type=ApplicantType.y.name)),
        j_appeals_cnt=Count('applicant_type', filter=Q(applicant_type=ApplicantType.j.name)),

        tal_appeals_cnt=Count('applicant_position', filter=Q(applicant_position=ApplicantPosition.tal.name)),
        oon_appeals_cnt=Count('applicant_position', filter=Q(applicant_position=ApplicantPosition.oon.name)),
        oqi_appeals_cnt=Count('applicant_position', filter=Q(applicant_position=ApplicantPosition.oqi.name)),
        uni_appeals_cnt=Count('applicant_position', filter=Q(applicant_position=ApplicantPosition.uni.name)),
        tas_appeals_cnt=Count('applicant_position', filter=Q(applicant_position=ApplicantPosition.tas.name)),
        bos_appeals_cnt=Count('applicant_position', filter=Q(applicant_position=ApplicantPosition.bos.name)),

        tas_country_appeals_cnt=Count('applicant_province', filter=Q(applicant_province=Provinces.tas.name)),
        sam_country_appeals_cnt=Count('applicant_province', filter=Q(applicant_province=Provinces.sam.name)),
        an_country_appeals_cnt=Count('applicant_province', filter=Q(applicant_province=Provinces.an.name)),
        far_country_appeals_cnt=Count('applicant_province', filter=Q(applicant_province=Provinces.far.name)),
        nam_country_appeals_cnt=Count('applicant_province', filter=Q(applicant_province=Provinces.nam.name)),
        qash_country_appeals_cnt=Count('applicant_province', filter=Q(applicant_province=Provinces.qash.name)),
        sur_country_appeals_cnt=Count('applicant_province', filter=Q(applicant_province=Provinces.sur.name)),
        bux_country_appeals_cnt=Count('applicant_province', filter=Q(applicant_province=Provinces.bux.name)),
        nav_country_appeals_cnt=Count('applicant_province', filter=Q(applicant_province=Provinces.nav.name)),
        xor_country_appeals_cnt=Count('applicant_province', filter=Q(applicant_province=Provinces.xor.name)),
        sir_country_appeals_cnt=Count('applicant_province', filter=Q(applicant_province=Provinces.sir.name)),
        jiz_country_appeals_cnt=Count('applicant_province', filter=Q(applicant_province=Provinces.jiz.name)),
        qor_country_appeals_cnt=Count('applicant_province', filter=Q(applicant_province=Provinces.qor.name)),
    )
    appeal_directions = AppealDirection.objects.annotate(cnt_appeals=Count('appeal', distinct=True))
    admins = CustomUser.objects.annotate(cnt_answers=Count('answer', distinct=True))
    answer_address_cnt = Answer.objects.aggregate(
        site_cnt=Count('answer_address', filter=Q(answer_address=AnswerAddress.s.name)),
        email_cnt=Count('answer_address', filter=Q(answer_address=AnswerAddress.e.name)),
        site_email_cnt=Count('answer_address', filter=Q(answer_address=AnswerAddress.se.name))
    )

    context = {
        'appeal_cnt_by_choices': appeal_cnt_by_choices,
        'admins': admins,
        'answer_address_cnt': answer_address_cnt,
        # 'new_appeals_cnt': new_appeals_cnt,
        #
        # # APPEAL TYPE
        # 'appeal_type': Appeal.APPEAL_TYPE,
        # 'appeal_type_cnt': list(appeal_type.values()),
        #
        # # ANSWER AUTHOR
        # 'admin_names': list(admins.keys()),
        # 'admin_cnt': list(admins.values()),
        #
        # # APPLICANT TYPE
        # 'applicant_type': Appeal.APPLICANT_TYPE,
        # 'applicant_type_cnt': list(applicant_type.values()),
        #
        # # APPLICANT POSITION
        # 'applicant_position': Appeal.APPLICANT_POSITION,
        # 'applicant_position_cnt': list(applicant_position.values()),
        #
        # # APPEAL STATUS
        'appeal_status': AppealStatus.get_values(),
        # 'appeal_status_cnt': list(appeal_status.values()),
        'appeal_status_cnt': appeal_cnt_by_choices.values(),
        #
        # # APPEAL DIRECTION
        # 'appeal_direction': Appeal.APPEAL_DIRECTION,
        # 'appeal_direction_cnt': list(appeal_direction.values()),
        #
        # # ANSWER ADDRESSES
        # 'answer_address': Answer.ANSWER_ADDRESS,
        # 'answer_address_cnt': list(answer_address.values()),
        #
        # # APPEAL COUNTRIES
        # 'appeal_country': list(appeal_country.values()),
    }

    return render(request, 'adminPanel/dashboard.html', context)


def admin_login(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)

            return redirect('dashboard')

        else:
            messages.error(request, "Login yoki parol noto'g'ri")

            return redirect('login')

    return render(request, 'adminPanel/login.html')


def profile(request, username):
    user = CustomUser.objects.get(username=username)
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
