from django.db import models
from django.db.models import JSONField


# Create your models here.
class Mod(models.Model):
    col = models.CharField(max_length=30)