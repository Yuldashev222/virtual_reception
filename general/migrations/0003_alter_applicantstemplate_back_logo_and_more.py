# Generated by Django 4.1.5 on 2023-01-07 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0002_rename_applicants_panel_applicantstemplate_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicantstemplate',
            name='back_logo',
            field=models.ImageField(blank=True, null=True, upload_to='Applicants_panel/images/'),
        ),
        migrations.AlterField(
            model_name='applicantstemplate',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='applicantstemplate',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='Applicants_panel/images/'),
        ),
    ]
