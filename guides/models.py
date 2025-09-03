from django.db import models
from accounts.models import User

class GuideProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, limit_choices_to={'role':'guide'})
    bio = models.TextField(null=True, blank=True)
    experience = models.TextField()
    languages = models.CharField(max_length=255)
    certifications = models.TextField()
    availability = models.TextField()
    profile_image = models.ImageField(upload_to='guide_images/', null=True, blank=True)

    def __str__(self):
        return self.user.username
