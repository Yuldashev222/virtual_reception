import os
import uuid
from django.core.validators import FileExtensionValidator
from django.db import models

from accounts.models import CustomUser
from .enums import (
    ApplicantType, AppealStatus, AppealType, ApplicantPosition, Provinces
)


class AppealDirection(models.Model):
    dip = "Diplom olish masalalari"
    ish = "Ishga joylash, ishdagi tortishuv, oylik maoshi"
    kon = "Kontrakt to'lovi to'g'risida"
    mag = "Magistratura masalalari"
    fuq = "Fuqarolar murojaatlari to'g'risida"
    mol = "Moliyaviy masalalar"
    tal = "Talaba ustidan shikoyat"
    rah = "Rahbar faoliyatidan norozilik arizasi"
    sti = "Stipendiya masalalari"
    oqk = "O'qishga kirish to'g'risida"
    oqc = "O'qishni ko'chirish to'g'risida"
    oqt = "O'qishni tiklash to'g'risida"
    ijo = "Ijodiy imtihondan norozilik to'g'risida"
    dix = "Diplom xaqqoniyligini tasdiqlab berish to'g'risida"
    naf = "Nafaqa masalalari"
    arx = "Arxiv ma'lumotlarini olish to'grisida"
    ikk = "Ikkinchi mutaxasislik"
    kit = "Kitob nashr qilish"
    ixt = "Ixtiro qilish taklifi"
    tak = "Taklif va minnatdorchilik"
    sir = "Sirtqi o'qish masalalari"
    yot = "Yotoqxona masalalari bo'yicha"
    oli = "Olimpiada masalasi bo'yicha"
    bos = "Boshqa yo'nalishlar"
    direction = models.CharField(max_length=200, unique=True)
    creator = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
    date_created = models.DateTimeField(auto_now_add=True)


class Appeal(models.Model):
    appeal_subject = models.CharField(max_length=60, blank=True)
    appeal_text = models.TextField(blank=True)
    appeal_file = models.FileField(
        upload_to='Appeal_Files/', blank=True, null=True,
        validators=[FileExtensionValidator(allowed_extensions=["pdf", "txt", "doc", "docx", "ppt", "xlsx", "xls"])]
    )
    appeal_type = models.CharField(max_length=1, choices=AppealType.choices())
    appeal_direction = models.ForeignKey(AppealDirection, on_delete=models.PROTECT)
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
        return self.applicant_full_name

    def filename(self):
        return os.path.basename(self.appeal_file.name)

# class AppealFile(models.Model):
#     appeal = models.ForeignKey(Appeal, on_delete=models.CASCADE)
#     appeal_file = models.FileField(
#         upload_to='Appeal_Files/',
#         blank=True,
#         validators=[FileExtensionValidator(allowed_extensions=["pdf", "txt", "doc", "docx", "ppt", "xlsx", "xls"])])
