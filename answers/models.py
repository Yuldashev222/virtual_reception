from django.db import models

from accounts.models import CustomUser
from appeals.models import Appeal
from .enums import AnswerType, AnswerAddress


class Answer(models.Model):
    appeal = models.ForeignKey(Appeal, on_delete=models.SET_NULL, null=True)
    author = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
    text = models.TextField(blank=True)
    file = models.FileField(upload_to='Answers/files/', blank=True, null=True)
    answer_type = models.CharField(max_length=1, choices=AnswerType.choices())
    answer_address = models.CharField(max_length=2, choices=AnswerAddress.choices())

    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        if self.appeal:
            return f'{self.appeal} murojaati javobi'
        return f'{self.author} javobi'
