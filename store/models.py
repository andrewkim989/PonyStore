from django.db import models
from django.core.exceptions import ValidationError

def nameValidation(value):
    if len(value) < 8:
        raise ValidationError (
            "Name must be at least 8 characters long"
        )

def priceValidation(value):
    if value < 0:
        raise ValidationError (
            "Price must be more than 0 bits"
        )

def descValidation(value):
    if len(value) > 100:
        raise ValidationError (
            "Description cannot be more than 100 characters long"
        )

class Product (models.Model):
    brand = models.CharField(max_length = 255)
    name = models.CharField(max_length = 255, verbose_name = "Product name",
        validators = [nameValidation])
    price = models.IntegerField(verbose_name = "Price (bits)", validators = [priceValidation])
    description = models.CharField(max_length = 255, validators = [descValidation])
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = models.Manager()