import os
import uuid
from ckeditor.fields import RichTextField
from django.core.validators import FileExtensionValidator
from django.db import models

from adminPanel.models import User


class Applicants_panel(models.Model):
    university_name = models.CharField(max_length=50)
    background = models.ImageField(upload_to="Applicants_panel/images/")
    logo = models.ImageField(upload_to="Applicants_panel/images/", blank=True)
    back_logo = models.ImageField(upload_to="Applicants_panel/images/", blank=True)
    title = models.CharField(max_length=50)
    sup_title = models.CharField(max_length=100)
    accept_text = RichTextField(blank=True)
    main_site_link = models.URLField()
    tel = models.CharField(blank=True, max_length=13)
    email = models.EmailField(blank=True)
    step_title_1 = models.CharField(max_length=50)
    step_title_2 = models.CharField(max_length=50)
    step_title_3 = models.CharField(max_length=50)
    aside_title = models.CharField(max_length=20)
    answer_title = models.CharField(max_length=30)
    statistics_title = models.CharField(max_length=30)

    # Rector infos
    rector_name = models.CharField(max_length=100)
    rector_avatar = models.ImageField(upload_to="Applicants_panel/images/")
    rector_position = models.CharField(max_length=100, blank=True)
    rector_reception_time = models.CharField(max_length=50, blank=True)
    updated_date = models.DateField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)


class Social(models.Model):
    name = models.CharField(max_length=50)
    link = models.URLField()
    logo = models.ImageField(upload_to="Applicants_panel/Social_images/")


class Appeal(models.Model):
    PROVINCE = [
        ('toshkent', 'Toshkent'),
        ('samarqand', 'Samarqand'),
        ('andijon', 'Andijon'),
        ('fargona', 'Fargona'),
        ('namangan', 'Namangan'),
        ('qashqadaryo', 'Qashqadaryo'),
        ('surxondaryo', 'Surxondaryo'),
        ('buxoro', 'Buxoro'),
        ('navoiy', 'Navoiy'),
        ('xorazm', 'Xorazm'),
        ('sirdaryo', 'Sirdaryo'),
        ('jizzax', 'Jizzax'),
        ('qoraqalpoq', 'Qoraqalpog\'iston Respublikasi'),
    ]

    APPEAL_TYPE = [
        ('ariza', 'Ariza'),
        ('shikoyat', 'Shikoyat'),
        ('taklif', 'Taklif'),
        ('boshqa', 'boshqa'),
    ]

    APPLICANT_POSITION = [
        ("talaba", "Talaba"),
        ("ota_ona", "Ota ona"),
        ("oqituvchi", "O'qituvchi"),
        ("universitet_xodimi", "Universitet xodimi"),
        ("tashkilot", "Tashkilot"),
        ("boshqa", "Boshqa"),
    ]

    APPLICANT_TYPE = [
        ('yuridik_shaxs', 'Yuridik shaxs'),
        ('jismoniy_shaxs', 'Jismoniy shaxs'),
    ]

    APPEAL_DIRECTION = [
        ("diplom_olish", "Diplom olish masalalari"),
        ("ishga_joylash", "Ishga joylash, ishdagi tortishuv, oylik maoshi"),
        ("kontrakt_tolovi", "Kontrakt to'lovi to'g'risida"),
        ("mag_masalalari", "Magistratura masalalari"),
        ("fuqarolar_murojaatlari", "Fuqarolar murojaatlari to'g'risida"),
        ("moliyaviy_masalalar", "Moliyaviy masalalar"),
        ("talaba_ustidan", "Talaba ustidan shikoyat"),
        ("rahbar_faoliyatidan", "Rahbar faoliyatidan norozilik arizasi"),
        ("stipendiya_masalalari", "Stipendiya masalalari"),
        ("oqishga_kirish", "O'qishga kirish to'g'risida"),
        ("oqishni_kochirish", "O'qishni ko'chirish to'g'risida"),
        ("oqishni_tiklash", "O'qishni tiklash to'g'risida"),
        ("ijodiy_imtihondan", "Ijodiy imtihondan norozilik to'g'risida"),
        ("diplom_xaqqoniyligini", "Diplom xaqqoniyligini tasdiqlab berish to'g'risida"),
        ("nafaqa_masalalari", "Nafaqa masalalari"),
        ("arxiv_malumotlarini", "Arxiv ma'lumotlarini olish to'grisida"),
        ("ikkinchi_mutaxasislik", "Ikkinchi mutaxasislik"),
        ("kitob_nashr", "Kitob nashr qilish"),
        ("ixtiro_qilish", "Ixtiro qilish taklifi"),
        ("taklif_va", "Taklif va minnatdorchilik"),
        ("sirtqi_oqish", "Sirtqi o'qish masalalari"),
        ("yotoqxona_masalalari", "Yotoqxona masalalari bo'yicha"),
        ("olimpiada_masalasi", "Olimpiada masalasi bo'yicha"),
        ("boshqa_yo", "Boshqa yo'nalishlar"),
    ]

    APPEAL_STATUS = [
        ('new', 'Yangi'),
        ('process', 'Ko\'rib chiqilmoqda'),
        ('rejected', 'Rad etilgan'),
        ('done', 'Bajarilgan'),
    ]

    appeal_subject = models.CharField(max_length=60, blank=True)
    appeal_text = models.TextField(blank=True)
    appeal_file = models.FileField(
        upload_to='Appeal_Files/',
        blank=True,
        validators=[FileExtensionValidator(allowed_extensions=["pdf", "txt", "doc", "docx", "ppt", "xlsx", "xls"])])
    appeal_type = models.CharField(max_length=10, choices=APPEAL_TYPE)
    appeal_direction = models.CharField(max_length=70, choices=APPEAL_DIRECTION)
    privacy = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    code = models.UUIDField(default=uuid.uuid4)
    appeal_status = models.CharField(max_length=10, choices=APPEAL_STATUS, default=APPEAL_STATUS[0][0])

    # APPLICANT DATA
    applicant_name = models.CharField(max_length=40)
    applicant_tel_num = models.CharField(max_length=13)
    applicant_email = models.EmailField(blank=True)
    applicant_province = models.CharField(max_length=40, choices=PROVINCE)
    applicant_type = models.CharField(max_length=15, choices=APPLICANT_TYPE)
    applicant_position = models.CharField(max_length=20, choices=APPLICANT_POSITION)

    def __str__(self):
        return self.applicant_name

    def filename(self):
        return os.path.basename(self.appeal_file.name)

    def get_cnt_country(country):
        return Appeal.objects.filter(applicant_province=country).count()

    def get_cnt_status(status):
        return Appeal.objects.filter(appeal_status=status).count()

    def get_cnt_direction(direction):
        return Appeal.objects.filter(appeal_direction=direction).count()


class Answer(models.Model):
    ACTIVE = [
        ('send', 'Yuborilsin'),
        ('save', 'Saqlab qo\'yilsin'),
    ]

    ANSWER_TYPE = [
        ('done', 'bajarildi'),
        ('rejected', 'rad etildi'),
    ]

    ANSWER_ADDRESS = [
        ('site', 'Sayt'),
        ('email', 'Email'),
        ('site_and_email', 'Sayt va Email'),
    ]

    text = models.TextField(blank=True)
    file = models.FileField(upload_to='Answers/files/', blank=True)
    appeal = models.ForeignKey(Appeal, on_delete=models.SET_NULL, related_name='get_answers', null=True)
    answer_type = models.CharField(max_length=10, choices=ANSWER_TYPE)
    answer_address = models.CharField(max_length=15, choices=ANSWER_ADDRESS)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    active = models.CharField(max_length=4, choices=ACTIVE)

    def __str__(self):
        if self.appeal:
            return f'{self.appeal} murojaati javobi'
        return f'{self.author} javobi'

    def get_cnt_answer_address(address):
        return Answer.objects.filter(answer_address=address).count()

    def filename(self):
        return os.path.basename(self.file.name)

    def updated_date_format(self):
        return self.updated_date.strftime('%d-%m-%Y || %H:%M')
