from django import forms

from .models import Appeal


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
            'applicant_full_name',
            'applicant_tel_num',
            'applicant_email',
            'applicant_province',
            'applicant_type',
            'applicant_position',
        ]
