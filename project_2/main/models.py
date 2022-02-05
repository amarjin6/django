from django.db import models
from django.db.models import JSONField


# Create your models here.
class Input(models.Model):
    data = models.CharField(max_length=30)
    convert = JSONField()

    def __str__(self):
        return self.data
