from django.db import models

# Create your models here.

class TOdo(models.Model):
    added_Date = models.DateTimeField()
    text = models.CharField(max_length=200)