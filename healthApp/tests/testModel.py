from django.test import TestCase
from healthApp.models import BG, Patient, Donor
from model_bakery import baker
from django.utils import timezone
class TestAppModels(TestCase):
    # def setUp(self):
    #     self.project1 = Donor.objects.create(
    #     Dname = "Donor1",
    #     blood_group = "O+",
    #     Dphone = 87654345678,
    #     Date = timezone.now,
    #     DateUpdate = timezone.now(),
    #     location = "",
    #     is_active = False,
    #     healthStatus = ""
    #     )
    def test_model_str(self):
        bg = BG.objects.create(
            info = "",
            bloodGroup = "O+",
        )
        bg.save()
        self.assertEqual(str(bg),"O+")
        donor = Donor(
            Dname = "Donor1",
            blood_group = bg,
            Dphone = 1234567,
            Date = timezone.now(),
            DateUpdate = timezone.now(),
            healthStatus = "Fine"
        )
        donor.save()
        self.assertEqual(str(donor), "Donor1")
        patient = Patient(
            Pname = "Patient2",
            blood_group = bg,
            Pphone = 1234567,
            Date = timezone.now(),
            DateUpdate = timezone.now(),
            healthIssue = ""
        )
        patient.save()
        self.assertEqual(str(patient), "Patient2")
        