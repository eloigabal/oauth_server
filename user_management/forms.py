from django.contrib.auth import password_validation
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError

from flexcoop_auth_server import settings


class SignUpForm(forms.ModelForm):
    password_confirm = forms.CharField(required=True)
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'password_confirm']

    def clean_password_confirm(self):
        password1 = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("password_confirm")
        if password1 != password2:
            self.add_error('password_confirm', "Password does not match")
        return password2

    def _post_clean(self):
        super(SignUpForm, self)._post_clean()
        # Validate the password after self.instance is updated with form data
        # by super().
        password = self.cleaned_data.get('password')
        try:
            password_validation.validate_password(password, self.instance)
        except forms.ValidationError as error:
            self.add_error('password_confirm', error)


class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
