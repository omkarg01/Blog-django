from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django import forms


class SignUpForm(UserCreationForm):
    # email = forms.EmailField(max_length=254, required=True, help_text='Required. Enter a valid email address.')
    password1 = forms.CharField(label=_("Password"),
        widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label=_("Password confirmation"),
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        help_text=_("Enter the same password as above, for verification."))
    
    class Meta:
        model = User
        fields = ['username', 'email','first_name', 'last_name', 'password1', 'password2']
        widgets = {
            'username' : forms.TextInput(attrs={'class': 'form-control'}),
            'email' : forms.EmailInput(attrs={'class': 'form-control'}),
            'first_name' : forms.TextInput(attrs={'class': 'form-control'}),
            'last_name' : forms.TextInput(attrs={'class': 'form-control'}),
        }

class LoginForm(AuthenticationForm):
    class Meta:
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
        }