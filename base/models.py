from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password) # Hash the password
        user.save(using=self._db)

        return user
    
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True')

        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=100, unique=True, blank=True, null=True)
    display_name = models.CharField(max_length=100, blank=True, null=True, default='Anonymous')
    bio = models.TextField(blank=True, null=True)
    # profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    # Required fields for Django User model
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = CustomUserManager() # Set our custom manager

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [] # Email & Password are required by default

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def get_full_name(self):
        return self.display_name
    
    def get_short_name(self):
        return self.display_name or self.email.split('@')[0]
    
    def __str__(self):
        return self.email
    
    def save(self, *args, **kwargs):
        if not self.username: # If no username is provided
            self.username = self.get_short_name()
        super().save(*args, **kwargs)


CustomUser = get_user_model()

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name.capitalize() # Keep original capitalization
    
    def save(self, *args, **kwargs):
        self.name = self.name.lower() # Store in lowercase for consistency
        super().save(*args, **kwargs)


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    def __str__(self):
        return self.name.capitalize()
    
    def save(self, *args, **kwargs):
        self.name = self.name.lower()
        super().save(*args, **kwargs)

class Post(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    tags = models.ManyToManyField(Tag, blank=True, related_name='posts')

    created_at = models.DateTimeField(auto_now_add=True)
    # Will add this when posts can be editted too.
    # updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-created_at'] # Newest first
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'