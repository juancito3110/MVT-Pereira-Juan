from django.db import models
from unittest.util import _MAX_LENGTH

class Familia(models.Model):
    nombre= models.CharField(max_length=40)
    edad= models.IntegerField()
    
