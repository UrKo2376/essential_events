from django.core import validators
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify
from django.conf import settings

# Create your models here.
class staticModel(models.Model):
    HOMESLIDER = "HS"
    HOMEHERO = "HH"
    MENULINK = "ML"
    OTHER = "OT"
    STATIC_MODEL_CHOICES = [
        (HOMESLIDER, "Home Slider"),
        (MENULINK, "Menu Link"),
        (OTHER, "Other"),
        (HOMEHERO, "Home Page Hero Details")
    ]

    name = models.CharField(max_length=50)
    description = models.CharField(max_length=400)
    staticType = models.CharField(max_length=2, choices=STATIC_MODEL_CHOICES, default=OTHER)
    image = models.ImageField(upload_to = 'staticModel/')
    slug = models.SlugField(default="", blank=-True, null=False, db_index=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

class menuItems(models.Model):
    displayName = models.CharField(max_length=20, null=False)
    slug = models.SlugField(default="", blank=-True, null=False, db_index=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)