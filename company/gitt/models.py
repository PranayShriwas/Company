from django.db import models

# Create your models here.


class Git(models.Model):
    pname = models.CharField(max_length=50)
    pemail = models.EmailField(max_length=254)
    pmobile = models.CharField(max_length=50)
    paddress = models.TextField()

    def __str__(self) -> str:
        return self.pname
