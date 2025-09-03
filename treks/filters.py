import django_filters
from django import forms
from django.db import models
from .models import Trek


class TrekFilter(django_filters.FilterSet):
    q = django_filters.CharFilter(method="search", label="Search")
    difficulty = django_filters.CharFilter(field_name="difficulty", lookup_expr="iexact")
    location = django_filters.CharFilter(field_name="location", lookup_expr="icontains")

    class Meta:
        model = Trek
        fields = ["q", "difficulty", "location"]

    def search(self, queryset, name, value):
        return queryset.filter(
            models.Q(name__icontains=value) | models.Q(description__icontains=value) | models.Q(location__icontains=value)
        )
