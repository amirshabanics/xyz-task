from django.core.validators import MinValueValidator
from django.db import models


# Create your models here.

class Index(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    index = models.FloatField(validators=[MinValueValidator(0)])
