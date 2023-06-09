from django.db import models

# Create your models here.


class Student(models.Model):
    Student_Reg_number = models.TextField()
    Student_name = models.CharField(max_length=50)
    Student_email = models.TextField()
    Student_mobile = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
