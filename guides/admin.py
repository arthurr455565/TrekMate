from django.contrib import admin
from .models import GuideProfile, TeamMember

@admin.register(GuideProfile)
class GuideProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'experience', 'languages')
    search_fields = ('user__username', 'languages', 'experience')


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'order', 'is_active', 'created_at')
    list_filter = ('is_active', 'created_at')
    search_fields = ('name', 'role', 'bio')
    list_editable = ('order', 'is_active')
    ordering = ('order', 'name')
