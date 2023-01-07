import os
import uuid
from django.core.validators import FileExtensionValidator
from django.db import models

from accounts.models import CustomUser
from .enums import (
    ApplicantType, AppealDirection, AppealStatus, AppealType, ApplicantPosition, Provinces
)


class Appeal(models.Model):
    appeal_subject = models.CharField(max_length=60, blank=True)
    appeal_text = models.TextField(blank=True)
    appeal_file = models.FileField(
        upload_to='Appeal_Files/', blank=True, null=True,
        validators=[FileExtensionValidator(allowed_extensions=["pdf", "txt", "doc", "docx", "ppt", "xlsx", "xls"])]
    )
    appeal_type = models.CharField(max_length=1, choices=AppealType.choices())
    appeal_direction = models.CharField(max_length=3, choices=AppealDirection.choices())
    privacy = models.BooleanField(default=False)
    code = models.UUIDField(default=uuid.uuid4)
    appeal_status = models.CharField(max_length=1, choices=AppealStatus.choices(), default=AppealStatus.n.name)

    # APPLICANT DATA
    applicant_full_name = models.CharField(max_length=40)
    applicant_tel_num = models.CharField(max_length=13)
    applicant_email = models.EmailField(blank=True, null=True)
    applicant_province = models.CharField(max_length=4, choices=Provinces.choices())
    applicant_type = models.CharField(max_length=1, choices=ApplicantType.choices())
    applicant_position = models.CharField(max_length=3, choices=ApplicantPosition.choices())

    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.applicant_name

    def filename(self):
        return os.path.basename(self.appeal_file.name)

# class AppealFile(models.Model):
#     appeal = models.ForeignKey(Appeal, on_delete=models.CASCADE)
#     appeal_file = models.FileField(
#         upload_to='Appeal_Files/',
#         blank=True,
#         validators=[FileExtensionValidator(allowed_extensions=["pdf", "txt", "doc", "docx", "ppt", "xlsx", "xls"])])
