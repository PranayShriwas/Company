from django.db import models

# Create your models here.


class Shoes(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    cat = models.CharField(max_length=50)
    cmp = models.CharField(max_length=50)
    size = models.IntegerField()

    def __str__(self) -> str:
        return self.name
