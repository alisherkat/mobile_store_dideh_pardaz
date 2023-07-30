from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=32)
    nationality = models.CharField(max_length=32)
