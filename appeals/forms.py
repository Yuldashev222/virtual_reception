from django import forms
from captcha.fields import CaptchaField

from .models import *


# captcha = CaptchaField()


class AppealForm(forms.ModelForm):
    class Meta:
        model = Appeal
        fields = [
            'appeal_subject',
            'appeal_text',
            'appeal_file',
            'appeal_type',
            'appeal_direction',
            'privacy',
            'applicant_name',
            'applicant_tel_num',
            'applicant_email',
            'applicant_province',
            'applicant_type',
            'applicant_position',
        ]


class ApplicantsPanelForm(forms.ModelForm):
    class Meta:
        model = Applicants_panel
        fields = [
            'background',
            'logo',
            'back_logo',
            'title',
            'tel',
            'email',
            'step_title_1',
            'step_title_2',
            'step_title_3',
            'rector_name',
            'rector_avatar',
            'rector_position',
            'rector_reception_time',
        ]
