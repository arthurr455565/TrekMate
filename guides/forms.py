from django import forms
from .models import GuideProfile

class GuideProfileForm(forms.ModelForm):
    class Meta:
        model = GuideProfile
        fields = ["bio", "experience", "languages", "certifications", "availability", "profile_image"]
        widgets = {
            "bio": forms.Textarea(attrs={"rows": 3}),
            "experience": forms.Textarea(attrs={"rows": 4}),
            "certifications": forms.Textarea(attrs={"rows": 3}),
            "availability": forms.Textarea(attrs={"rows": 2}),
        }
