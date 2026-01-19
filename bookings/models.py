from django.db import models
from django.conf import settings
from treks.models import Trek
from guides.models import GuideProfile


class Booking(models.Model):
    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Confirmed', 'Confirmed'),
        ('Cancelled', 'Cancelled'),
    )

    # User info (can be null if user not logged in)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    name = models.CharField(max_length=200, default='Guest')
    email = models.EmailField(default='noreply@trekmate.com')
    
    # Trek selections (stored as comma-separated values)
    selected_treks = models.TextField(help_text="Comma-separated trek names", default='')
    
    # Date preferences
    preferred_dates = models.TextField(help_text="User's preferred dates or time period", default='')
    
    # Experience and additional info
    hiking_experience = models.TextField(blank=True)
    additional_comments = models.TextField(blank=True)
    
    # Legacy fields (keeping for compatibility)
    guide = models.ForeignKey(
        GuideProfile,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    trek = models.ForeignKey(Trek, on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.email}) - {self.status}"


class Review(models.Model):
    booking = models.OneToOneField('Booking', on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField()  # 1-5
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        guide_name = self.booking.guide.user.username if self.booking.guide else "No guide"
        return f"{self.booking.trekker.username} -> {guide_name} ({self.rating})"
