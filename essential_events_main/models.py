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
    description = models.TextField(max_length=400)
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
        return self.displayName

    def save(self, *args, **kwargs):
        self.slug = slugify(self.displayName)
        super().save(*args, **kwargs)

class actsModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    category = models.CharField(max_length=2)
    main_image = models.ImageField(upload_to = 'actsModel/')
    slug = models.SlugField(default="", blank=-True, null=False, db_index=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

class actImages(models.Model):
    actName = models.ForeignKey(actsModel, default=None, on_delete=models.DO_NOTHING)
    altDescription = models.CharField(max_length = 50)
    image = models.ImageField(upload_to='actsModel/')
    slug = models.SlugField(default="", blank=-True, null=False, db_index=True)

    def __str__(self):
        return str(self.actName)

    def save(self, *args, **kwargs):
        self.slug = slugify(str(self.actName))
        super().save(*args, **kwargs)