from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError


class SignUpForm(forms.ModelForm):
    password_confirm = forms.CharField(required=True)
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'password_confirm']

    def clean(self):
        password = self.cleaned_data.get('password')
        password_confirm = self.cleaned_data.get('password_confirm')
        if password != password_confirm:
            raise ValidationError("Password and Password Confirm must match")
