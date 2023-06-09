from django.db import models

# Create your models here.


class Employee(models.Model):
    emplyee_regNo = models.TextField(unique=True)
    emplyee_name = models.TextField()
    emplyee_email = models.TextField()
    emplyee_mobile = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.emplyee_name
