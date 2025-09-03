from django.contrib import admin
from .models import Trek

@admin.register(Trek)
class TrekAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'difficulty', 'duration', 'altitude', 'best_season')
    search_fields = ('name', 'location', 'difficulty')
