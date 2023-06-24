from django.db import models

# Create your models here.


class Mobile(models.Model):
    Mobile_name = models.CharField(max_length=50)
    Mobile_price = models.IntegerField()
    Cat = models.CharField(max_length=50)
    Cmp = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.Mobile_name
