from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.base_user import BaseUserManager
from imagekit.models import ProcessedImageField, ImageSpecField
from phone_field import PhoneField
from pilkit.processors import ResizeToFill


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """

        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), max_length=200, unique=True)
    first_name = models.CharField(_('first name'), max_length=20, blank=False)
    last_name = models.CharField(_('last name'), max_length=20, blank=False)
    location = models.CharField(max_length=30, blank=True)
    phone = PhoneField(blank=True, help_text='Contact phone number', unique=True)
    birth_date = models.DateField(null=True, blank=True, db_index=True)
    bio = models.TextField(max_length=500, blank=True, null=True)

    avatar = ProcessedImageField(default='default_avatar.jpg',
                                 upload_to='avatars',
                                 processors=[ResizeToFill(200, 200)],
                                 format='JPEG',
                                 options={'quality': 80})

    avatar_thumbnail = ImageSpecField(source='avatar',
                                      processors=[ResizeToFill(50, 50)],
                                      format='JPEG',
                                      options={'quality': 80})

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    def __str__(self):
        return self.get_full_name()


