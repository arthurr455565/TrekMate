from django.db import models
from django.utils.text import slugify


class Trek(models.Model):
    DIFFICULTY_CHOICES = (
        ('Easy', 'Easy'),
        ('Moderate', 'Moderate'),
        ('Hard', 'Hard'),
    )

    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)  # ✅ Add this
    location = models.CharField(max_length=255)
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES)
    description = models.TextField()
    duration = models.CharField(max_length=50)
    altitude = models.IntegerField()
    best_season = models.CharField(max_length=50)
    image = models.ImageField(upload_to='trek_images/', null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
