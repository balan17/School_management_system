from django.db import models
from django.contrib.auth.models import User

class Staff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    staff_name = models.CharField(max_length=100)
    staff_salary = models.DecimalField(max_digits=10, decimal_places=2)
    staff_work = models.CharField(max_length=200)
    profile_picture = models.ImageField(upload_to='staff_profile_pics/', null=True, blank=True)


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    student_name = models.CharField(max_length=100)
    student_fees = models.DecimalField(max_digits=10, decimal_places=2)
    joining_date = models.DateField()
    profile_picture = models.ImageField(upload_to='student_profile_pics/', null=True, blank=True)

