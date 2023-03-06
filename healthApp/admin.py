from django.contrib import admin
from healthApp.models import BG, Donor, Patient

# Register your models here.
model_list = [BG, Donor, Patient]
admin.site.register(model_list)
