from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )


class ProfileForm(UserChangeForm):
    username = forms.CharField(max_length=30, widget=forms.TextInput(attrs=dict(
        readonly='readonly')))

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        del self.fields['password']

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'bio', 'location', 'birth_date')
