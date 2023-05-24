from django.db import models

# Create your models here.
from django.db import models

class Character(models.Model):
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    house = models.CharField(max_length=50)
    patronus = models.CharField(max_length=50)
    # Añade más campos según tus necesidades
