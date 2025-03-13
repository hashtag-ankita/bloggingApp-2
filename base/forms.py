from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model

CustomUser = get_user_model()

class SignupForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']

    def clean_username(self):
        if not self.cleaned_data['username']:
            raise forms.ValidationError("Please enter a username.")
        username = self.cleaned_data['username']

        # replace the spaces with underscores
        cleaned_username = username.replace(' ', '_')

        # Ensure the username is unique
        original_username = cleaned_username.lower()
        count = 1
        while CustomUser.objects.filter(username=cleaned_username).exists():
            cleaned_username = f'{original_username}_{count}'
            count += 1

        if cleaned_username != username:
            self.cleaned_data['username'] = cleaned_username # Update the cleaned data with the new username

        return cleaned_username
    

    def clean_email(self):
        email = self.cleaned_data.get('email').strip().lower() # Normalize the email address
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already registered. Try logging in instead.")
        return email


class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

    def clean_email(self):
        return self.cleaned_data['email'].lower()  # Normalize email