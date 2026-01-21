from django.contrib import admin
from .models import Booking
from .models import Review


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'user', 'selected_treks', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('name', 'email', 'user__username', 'selected_treks')
    list_editable = ('status',) 

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('booking', 'rating', 'created_at')
    search_fields = ('booking__name', 'booking__email')
