from django.db import models
from ckeditor.fields import RichTextField

from accounts.models import CustomUser


class ApplicantsTemplate(models.Model):
    university_name = models.CharField(max_length=50)
    background = models.ImageField(upload_to="Applicants_panel/images/")
    logo = models.ImageField(upload_to="Applicants_panel/images/", blank=True, null=True)
    back_logo = models.ImageField(upload_to="Applicants_panel/images/", blank=True, null=True)
    title = models.CharField(max_length=50)
    sup_title = models.CharField(max_length=100)
    accept_text = RichTextField(blank=True)
    main_site_link = models.URLField()
    tel = models.CharField(blank=True, max_length=13)
    email = models.EmailField(blank=True, null=True)
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
    author = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)


class EduSocial(models.Model):
    name = models.CharField(max_length=50)
    link = models.URLField()
    logo = models.ImageField(upload_to="Applicants_panel/Social_images/")
