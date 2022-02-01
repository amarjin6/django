from django.db import models
from django.db.models import JSONField


# Create your models here.
class Input(models.Model):
    field = models.CharField(max_length=50)
    data = JSONField()


def __str__(self):
    return self.data, self.field
