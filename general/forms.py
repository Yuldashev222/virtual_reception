from django import forms

from .models import ApplicantsTemplate


class ApplicantsPanelForm(forms.ModelForm):
    class Meta:
        model = ApplicantsTemplate
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
