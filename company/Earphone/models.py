from django.db import models
# Create your models here.

C_choice = (('Black', "Black"), ('Red', "Red"),
        ('white', "white"), ('Green', "Green")
        )


class Earphone(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    cat = models.CharField(max_length=50)
    cmp = models.CharField(max_length=50)
    color = models.CharField(choices=C_choice, max_length=50)

    def __str__(self) -> str:
        return self.name


