from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.db import models
from django.shortcuts import reverse
from django.core.validators import MinLengthValidator
from rest_framework.reverse import reverse as api_reverse


class CustomUser(AbstractUser):
    username_validator = MinLengthValidator(
        limit_value=5,
        message="Username must be at least 5 characters long."
    )

    username = models.CharField(
        'username',
        max_length=30,
        unique=True,
        help_text='Required. Must have at least 5 characters.',
        validators=[username_validator],
        error_messages={
            'unique': "A user with that username already exists.",
        },
    )

    email = models.EmailField('email address', blank=False)

    def get_api_url(self, request=None):
        return api_reverse(request=request, viewname='user-rud', kwargs={'pk': self.pk})


class Profile(models.Model):
    user = models.OneToOneField(to=get_user_model(), primary_key=True, on_delete=models.CASCADE)
    image = models.ImageField(default='profile_pics/profile.png', upload_to='profile_pics')

    def get_absolute_url(self):
        return reverse(viewname='profile', kwargs=self.pk)

    def __str__(self):
        return self.user.username + "'s Profile"
