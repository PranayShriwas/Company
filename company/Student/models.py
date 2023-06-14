from django.db import models

# Create your models here.


class Student(models.Model):
    Student_Reg_number = models.TextField(unique=True)
    Student_name = models.CharField(max_length=50)
    Student_email = models.TextField()
    Student_mobile = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now=True)
    password = models.CharField(max_length=250)

    def __str__(self) -> str:
        return self.Student_name
