from django.contrib.auth.forms import forms, UserCreationForm
from django.contrib.auth import get_user_model
from .models import Profile


class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'password1', 'password2']


class UserEditForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['username', 'email']
