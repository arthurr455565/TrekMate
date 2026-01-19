from django import forms
from .models import Booking, Review
from guides.models import GuideProfile


class TrekBookingForm(forms.ModelForm):
    TREK_CHOICES = [
        ('poonhill', 'Poonhill - Ghandruk Trek'),
        ('annapurna_base_camp', 'Annapurna Base Camp'),
        ('annapurna_circuit', 'Annapurna Circuit'),
        ('everest_base_camp', 'Everest Base Camp'),
        ('langtang_valley', 'Langtang Valley'),
        ('langtang_gosaikund', 'Langtang Valley via Gosaikund Sacred Lakes'),
        ('manaslu_circuit', 'Manaslu Circuit'),
        ('dolpo_jumla', 'Dolpo to Jumla via Kagmara Pass'),
        ('custom', 'Mustang, Dhaulagiri, Dolpo, Jumla, Kanchenjunga etc'),
    ]
    
    name = forms.CharField(
        max_length=200,
        widget=forms.TextInput(attrs={
            'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-trek-blue focus:border-transparent',
            'placeholder': 'Your full name'
        })
    )
    
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-trek-blue focus:border-transparent',
            'placeholder': 'your.email@example.com'
        })
    )
    
    treks = forms.MultipleChoiceField(
        choices=TREK_CHOICES,
        widget=forms.CheckboxSelectMultiple(attrs={
            'class': 'mr-2'
        }),
        required=True
    )
    
    preferred_dates = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-trek-blue focus:border-transparent',
            'placeholder': 'e.g., April 2025, October 15-30, 2025, or "Flexible"',
            'rows': 2
        }),
        help_text='You can trek almost any time in Nepal. April and October usually have the best visibility/views, but also the most people.'
    )
    
    hiking_experience = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-trek-blue focus:border-transparent',
            'placeholder': 'Describe your hiking/trekking experience and altitude experience',
            'rows': 3
        }),
        required=False
    )
    
    additional_comments = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-trek-blue focus:border-transparent',
            'placeholder': 'Any questions, concerns, or special requirements?',
            'rows': 3
        }),
        required=False
    )
    
    class Meta:
        model = Booking
        fields = ['name', 'email', 'preferred_dates', 'hiking_experience', 'additional_comments']
    
    def save(self, commit=True, user=None):
        booking = super().save(commit=False)
        booking.selected_treks = ', '.join(self.cleaned_data['treks'])
        if user and user.is_authenticated:
            booking.user = user
        if commit:
            booking.save()
        return booking


class BookingForm(forms.ModelForm):
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Booking
        fields = ['trek', 'guide', 'date']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['guide'].queryset = GuideProfile.objects.filter(availability=True)
        self.fields['guide'].required = False


class ReviewForm(forms.ModelForm):
    rating = forms.IntegerField(min_value=1, max_value=5)

    class Meta:
        model = Review
        fields = ['rating', 'comment']
        widgets = {
            'comment': forms.Textarea(attrs={'rows': 3}),
        }
