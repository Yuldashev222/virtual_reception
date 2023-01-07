from django import forms

from .models import Answer


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ["text", "file", "appeal", "answer_type", "answer_address", "active"]
