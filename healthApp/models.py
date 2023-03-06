from django.db import models
from django.utils import timezone

# Create your models here.
class BG(models.Model):
    groupNames = (
        ('A+', 'A+'),
        ('O+','O+'),
        ('B+','B+'),
        ('AB+','AB+'),
        ('A-','A-'),
        ('O-','O-'),
        ('B-','B-'),
        ('AB-', 'AB-'),
    )

    info = models.TextField()
    bloodGroup = models.CharField(max_length=100, choices=groupNames)

    class Meta:
        verbose_name = "Blood Group"
        verbose_name_plural = "Blood Groups"
    
    def __str__(self):
        return f"{self.bloodGroup}"
    
class Donor(models.Model):
    Dname = models.CharField(max_length=120, verbose_name="Name")
    blood_group = models.ForeignKey(BG, on_delete=models.CASCADE, default="")
    Dphone = models.IntegerField()
    Date = models.DateTimeField(auto_now_add=True)
    DateUpdate = models.DateTimeField(auto_now=True)
    location = models.CharField(max_length=100, default=" ")
    is_active = models.BooleanField(default=False)
    healthStatus = models.TextField(default=None)

    def __str__(self):
        return f"{self.Dname}" 
    
    class Meta:
        verbose_name = "Donor"
        verbose_name_plural = "Donors"

class Patient(models.Model):
    Pname = models.CharField(max_length=120, verbose_name="Patient")
    blood_group = models.ForeignKey(BG, on_delete=models.CASCADE)
    Pphone = models.IntegerField()
    Date = models.DateTimeField(auto_now_add=True)
    DateUpdate = models.DateTimeField(auto_now=True)
    hospital = models.CharField(max_length=120, blank=False, default="General Hospital")
    doctorName = models.CharField(max_length=120, blank=False, default="Dr. John Doe")
    healthIssue = models.TextField(default=None)
    is_patient = models.BooleanField(default=False)

    def __str__(self):
        return self.Pname
    
    class Meta:
        verbose_name = "Patient"
        verbose_name_plural = "Patients"
