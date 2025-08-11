from django.db import models
from django.utils.text import slugify


class Service(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    starting_price = models.DecimalField(max_digits=8, decimal_places=2)
    duration_text = models.CharField(max_length=100, blank=True)
    features = models.JSONField(default=list, blank=True)
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Package(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    starting_price = models.DecimalField(max_digits=8, decimal_places=2)
    duration_text = models.CharField(max_length=100, blank=True)
    includes = models.JSONField(default=list, blank=True)
    perfect_for = models.CharField(max_length=255, blank=True)
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class AddOn(models.Model):
    name = models.CharField(max_length=100)
    price_range = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class SiteSettings(models.Model):
    company_name = models.CharField(max_length=255)
    tagline = models.CharField(max_length=255)
    phone = models.CharField(max_length=50)
    email = models.EmailField()
    service_area = models.CharField(max_length=255)
    hours_text = models.CharField(max_length=255)
    cancellation_policy = models.TextField()
    weather_policy = models.TextField()
    heavy_policy = models.TextField()
    guarantee_policy = models.TextField()
    theme_bg = models.CharField(max_length=7, default="#1a1a1a")
    theme_accent = models.CharField(max_length=7, default="#7B2A2A")

    def save(self, *args, **kwargs):
        self.pk = 1  # enforce singleton
        super().save(*args, **kwargs)

    @classmethod
    def load(cls):
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj

    def __str__(self):
        return "Site Settings"
