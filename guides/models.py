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


class TeamMember(models.Model):
    name = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    bio = models.TextField()
    image_url = models.URLField(max_length=500, help_text="URL to team member's photo")
    order = models.IntegerField(default=0, help_text="Display order (lower numbers appear first)")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', 'name']

    def __str__(self):
        return f"{self.name} - {self.role}"
