from django.db import models

# Create your models here.


class Bag(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    cat = models.CharField(max_length=50)
    cmp = models.CharField(max_length=50)

    def __str__(self):
        return self.name
