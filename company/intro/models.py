from django.db import models

# Create your models here.
class Intro(models.Model):
    name=models.CharField( max_length=50)
    email=models.EmailField( max_length=254)
    phone_no=models.IntegerField()
    add=models.TextField()
    def __str__(self) -> str:
        return self.name
    
