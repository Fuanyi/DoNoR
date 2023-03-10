# Generated by Django 4.1.4 on 2023-02-24 09:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('healthApp', '0006_patient_doctorname_patient_hospital'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='Date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patient',
            name='DateUpdate',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='donor',
            name='Date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
