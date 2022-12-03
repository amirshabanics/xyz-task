from django.core.validators import MinValueValidator
from django.db import models


# Create your models here.

class Index(models.Model):
    datetime = models.DateTimeField()
    index = models.FloatField(validators=[MinValueValidator(0)])
