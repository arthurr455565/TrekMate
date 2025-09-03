from django.contrib import admin
from .models import Booking
from .models import Review


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('trekker', 'guide', 'trek', 'date', 'status', 'created_at')
    list_filter = ('status', 'date')
    search_fields = ('trekker__username', 'guide__user__username', 'trek__name')

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('booking', 'rating', 'created_at')
    search_fields = ('booking__trekker__username', 'booking__guide__user__username')
