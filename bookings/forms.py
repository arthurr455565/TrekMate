from django import forms
from .models import Booking, Review
from guides.models import GuideProfile   # ✅ import GuideProfile


class BookingForm(forms.ModelForm):
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Booking
        fields = ['trek', 'guide', 'date']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # ✅ Only list available guides
        self.fields['guide'].queryset = GuideProfile.objects.filter(availability=True)
        # ✅ Make guide optional
        self.fields['guide'].required = False


class ReviewForm(forms.ModelForm):
    rating = forms.IntegerField(min_value=1, max_value=5)

    class Meta:
        model = Review
        fields = ['rating', 'comment']
        widgets = {
            'comment': forms.Textarea(attrs={'rows': 3}),
        }
