# Generated by Django 4.0.3 on 2022-04-13 11:59

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appeals', '0005_alter_appeal_appeal_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='file',
            field=models.FileField(blank=True, upload_to='Answers/files/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf', 'txt', 'doc', 'docx', 'ppt'])]),
        ),
        migrations.AlterField(
            model_name='appeal',
            name='appeal_file',
            field=models.FileField(blank=True, upload_to='Appeal Files/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf', 'txt', 'doc', 'docx', 'ppt'])]),
        ),
    ]
