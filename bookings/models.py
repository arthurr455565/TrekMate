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

    trekker = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        limit_choices_to={'role': 'trekker'}
    )
    guide = models.ForeignKey(
        GuideProfile,
        on_delete=models.SET_NULL,   # guide optional
        null=True,
        blank=True
    )
    trek = models.ForeignKey(Trek, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        guide_name = self.guide.user.username if self.guide else "No guide"
        return f"{self.trekker.username} -> {guide_name} ({self.trek.name})"


class Review(models.Model):
    booking = models.OneToOneField('Booking', on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField()  # 1-5
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        guide_name = self.booking.guide.user.username if self.booking.guide else "No guide"
        return f"{self.booking.trekker.username} -> {guide_name} ({self.rating})"
