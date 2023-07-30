from django.core.validators import MinValueValidator
from django.db import models


class Mobile(models.Model):
    brand = models.ForeignKey("Brand", on_delete=models.CASCADE, related_name="sub_mobile")
    model_name = models.CharField(max_length=128, unique=True)
    price = models.FloatField(validators=[MinValueValidator(0.0)])
    size = models.FloatField(validators=[MinValueValidator(0.0)])
    color = models.CharField(max_length=32)
    is_available = models.BooleanField()
    country = models.CharField(max_length=32)

