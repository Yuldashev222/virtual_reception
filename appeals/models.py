from email.policy import default
from phonenumber_field.modelfields import PhoneNumberField
import uuid
from django.db import models

from adminPanel.models import User

class Applicants_panel(models.Model):
    background = models.ImageField(upload_to="Applicants panel/images/")
    logo = models.ImageField(upload_to="Applicants panel/images/", blank=True)
    back_logo = models.ImageField(upload_to="Applicants panel/images/", blank=True)
    title = models.CharField(max_length=50)
    tel = PhoneNumberField(blank=True)
    email = models.EmailField(blank=True)
    step_title_1 = models.CharField(max_length=50)
    step_title_2 = models.CharField(max_length=50)
    step_title_3 = models.CharField(max_length=50)

    # Rector infos
    rector_name = models.CharField(max_length=100)
    rector_avatar = models.ImageField(upload_to="Applicants panel/images/")
    rector_position = models.CharField(max_length=100, blank=True)
    rector_reception_time = models.CharField(max_length=50, blank=True)
    updated_date = models.DateField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)


class Social(models.Model):
    name = models.CharField(max_length=50)
    link = models.URLField()
    logo = models.ImageField(upload_to="Applicants panel/Social images/")
    

class Appeal(models.Model):
    
    PROVINCE = [
        ('Toshkent', 'Toshkent'),
        ('Samarqand', 'Samarqand'),
        ('Andijon', 'Andijon'),
        ('Fargona', 'Fargona'),
        ('Namangan', 'Namangan'),
        ('Qashqadaryo', 'Qashqadaryo'),
        ('Surxondaryo', 'Surxondaryo'),
        ('Buxoro', 'Buxoro'),
        ('Navoiy', 'Navoiy'),
        ('Xorazm', 'Xorazm'),
        ('Sirdaryo', 'Sirdaryo'),
        ('Jizzax', 'Jizzax'),
        ('Qoraqalpog\'iston Respublikasi', 'Qoraqalpog\'iston Respublikasi'),
    ]
    
    APPEAL_TYPE = [
        ('Ariza', 'Ariza'),
        ('Shikoyat', 'Shikoyat'),
        ('Taklif', 'Taklif'),
        ('boshqa', 'boshqa'),
    ]
    APPLICANT_POSITION = [
        ("Talaba", "Talaba"),
        ("Ota ona", "Ota ona"),
        ("Universitet xodimi", "Universitet xodimi"),
        ("Tashkilot", "Tashkilot"),
        ("Boshqa", "Boshqa"),
    ]
    
    APPLICANT_TYPE = [
        ('Yuridik_shaxs', 'Yuridik shaxs'),
        ('Jismoniy_shaxs', 'Jismoniy shaxs'),
    ]
    
    APPEAL_DIRECTION = [
        ("Diplom olish masalalari", "Diplom olish masalalari"),
        ("Ishga joylash, ishdagi tortishuv, oylik maoshi", "Ishga joylash, ishdagi tortishuv, oylik maoshi"),
        ("Kontrakt to'lovi to'g'risida", "Kontrakt to'lovi to'g'risida"),
        ("Magistratura masalalari", "Magistratura masalalari"),
        ("Fuqarolar murojaatlari to'g'risida", "Fuqarolar murojaatlari to'g'risida"),
        ("Moliyaviy masalalar", "Moliyaviy masalalar"),
        ("Talaba ustidan shikoyat", "Talaba ustidan shikoyat"),
        ("Rahbar faoliyatidan norozilik arizasi", "Rahbar faoliyatidan norozilik arizasi"),
        ("Stipendiya masalalari", "Stipendiya masalalari"),
        ("O'qishga kirish to'g'risida", "O'qishga kirish to'g'risida"),
        ("O'qishni ko'chirish to'g'risida", "O'qishni ko'chirish to'g'risida"),
        ("O'qishni tiklash to'g'risida", "O'qishni tiklash to'g'risida"),
        ("Ijodiy imtihondan norozilik to'g'risida", "Ijodiy imtihondan norozilik to'g'risida"),
        ("Diplom xaqqoniyligini tasdiqlab berish to'g'risida", "Diplom xaqqoniyligini tasdiqlab berish to'g'risida"),
        ("Nafaqa masalalari", "Nafaqa masalalari"),
        ("Arxiv ma'lumotlarini olish to'grisida", "Arxiv ma'lumotlarini olish to'grisida"),
        ("Ikkinchi mutaxasislik", "Ikkinchi mutaxasislik"),
        ("Kitob nashr qilish", "Kitob nashr qilish"),
        ("Ixtiro qilish taklifi", "Ixtiro qilish taklifi"),
        ("Taklif va minnatdorchilik", "Taklif va minnatdorchilik"),
        ("Sirtqi o'qish masalalari", "Sirtqi o'qish masalalari"),
        ("Yotoqxona masalalari bo'yicha", "Yotoqxona masalalari bo'yicha"),
        ("Olimpiada masalasi bo'yicha", "Olimpiada masalasi bo'yicha"),
        ("Boshqa yo'nalishlar", "Boshqa yo'nalishlar"),
    ]
    
    appeal_subject = models.CharField(max_length=60)
    appeal_text = models.TextField()
    appeal_file = models.FileField(upload_to='Appeal Files/', blank=True)
    appeal_type = models.CharField(max_length=10, choices=APPEAL_TYPE)
    appeal_direction = models.CharField(max_length=70, choices=APPEAL_DIRECTION)
    privacy = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    code = models.UUIDField(default=uuid.uuid4)

    # APPLICANT DATA
    applicant_name = models.CharField(max_length=40)
    applicant_tel_num = PhoneNumberField()
    applicant_email = models.EmailField(blank=True)
    applicant_province = models.CharField(max_length=40, choices=PROVINCE)
    applicant_type = models.CharField(max_length=15, choices=APPLICANT_TYPE)
    applicant_position = models.CharField(max_length=20, choices=APPLICANT_POSITION)


    def __str__(self):
        return self.applicant_name


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
    
    text = models.TextField()
    file = models.FileField(upload_to='Answers/files/', blank=True)
    appeal = models.ForeignKey(Appeal, on_delete=models.SET_NULL, null=True)
    answer_type = models.CharField(max_length=10, choices=ANSWER_TYPE)
    answer_address = models.CharField(max_length=15, choices=ANSWER_ADDRESS)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    active = models.CharField(max_length=4, choices=ACTIVE)
    
    