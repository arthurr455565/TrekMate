from django.contrib import admin
from .models import GuideProfile

@admin.register(GuideProfile)
class GuideProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'experience', 'languages')
    search_fields = ('user__username', 'languages', 'experience')
