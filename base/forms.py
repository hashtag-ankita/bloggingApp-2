from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from .models import Post, Category, Tag

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
    

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['profile_picture', 'username', 'display_name', 'email', 'bio']
        widgets = {
            'profile_picture': forms.ClearableFileInput()
        }

    def clean_username(self):
        if not self.cleaned_data['username']:
            raise forms.ValidationError("Please enter a new username.")
        username = self.cleaned_data['username']

        # replace the spaces with underscores
        cleaned_username = username.replace(' ', '_').lower()
        
        # raise an error if the new username already exists, regardless of the case
        if CustomUser.objects.filter(username__iexact=cleaned_username).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError("Username not available. Please choose another one.")
        
        return cleaned_username
    
    def clean_email(self):
        email = self.cleaned_data.get('email').strip().lower() # Normalize the email address

        if CustomUser.objects.filter(email=email).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError("This email is already registered. Try using another email.")
        
        return email
        
    def save(self, commit=True):
        user = super().save(commit=False)

        # Handle clearing the picture
        if self.cleaned_data.get('profile_picture') is False:
            if user.profile_picture:
                user.profile_picture.delete(save=False)
            user.profile_picture = None

        # if new picture uploaded, delete the old one
        elif self.cleaned_data.get('profile_picture'):
            # if an old picture exists and is different, delete it
            if self.instance.profile_picture and self.instance.profile_picture != self.cleaned_data.get('profile_picture'):
                self.instance.profile_picture.delete(save=False)

            user.profile_picture = self.cleaned_data.get('profile_picture')
        
        if commit:
            user.save()
        return user

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'category', 'tags']

    title = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter the title',
        })
    )

    content = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Enter the content',
        })
    )

    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        empty_label="Select a category",
        widget=forms.Select(attrs={
            'class': 'form-control',
        })
    )

    tags = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter tags separated by commas',
        })
    )

    def clean_tags(self):
        '''Optional: Validate and process the tags field, if provided'''
        tags_input = self.cleaned_data.get('tags', '')
        tags_list = [tag.strip() for tag in tags_input.split(',') if tag.strip()]
        return tags_list # Return a list of clean tags
    

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

    name = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter the category name',
        })
    )

    def clean_name(self):
        name = self.cleaned_data.get('name', '').strip() # Normalize the category name
        if Category.objects.filter(name__iexact=name).exists(): # Case-insensitive check
            raise forms.ValidationError("This category name already exists!")
        return name # Return the cleaned category name