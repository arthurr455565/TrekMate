from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm

User = get_user_model()

# Registration form
class RegisterForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-trek-blue focus:border-transparent transition',
            'placeholder': 'Enter your password'
        }),
        label='Password'
    )
    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(attrs={
            'class': 'w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-trek-blue focus:border-transparent transition',
            'placeholder': 'Confirm your password'
        })
    )

    class Meta:
        model = User
        fields = ["username", "email"]  # Removed 'role' from fields
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-trek-blue focus:border-transparent transition',
                'placeholder': 'Choose a username'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-trek-blue focus:border-transparent transition',
                'placeholder': 'your.email@example.com'
            })
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already registered.")
        return email

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password2 = cleaned_data.get("password2")

        if password and password2 and password != password2:
            self.add_error("password2", "Passwords do not match")
        return cleaned_data
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = 'trekker'  # Automatically set role to trekker
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


# Login form
class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label="Username",
        widget=forms.TextInput(attrs={
            'class': 'w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-trek-blue focus:border-transparent transition',
            'placeholder': 'Enter your username'
        })
    )
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={
            'class': 'w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-trek-blue focus:border-transparent transition',
            'placeholder': 'Enter your password'
        })
    )
