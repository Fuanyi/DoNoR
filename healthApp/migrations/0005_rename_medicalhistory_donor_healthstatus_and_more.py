# Generated by Django 4.1.4 on 2023-02-20 09:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('healthApp', '0004_alter_bg_bloodgroup'),
    ]

    operations = [
        migrations.RenameField(
            model_name='donor',
            old_name='medicalHistory',
            new_name='healthStatus',
        ),
        migrations.RenameField(
            model_name='patient',
            old_name='medicalHistory',
            new_name='healthIssue',
        ),
    ]
