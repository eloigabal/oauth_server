from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from user_management.forms import SignUpForm

# Create your views here.
from user_management.models import FlexUser


class SignupView(CreateView):
    model = User
    template_name= "registration/signup.html"
    form_class = SignUpForm
    success_url = reverse_lazy('user_management:success')

    def form_valid(self, form):
        response = super(SignupView, self).form_valid(form)
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        user.save()
        profile = FlexUser()
        profile.user = user
        profile.get_anonimizedID()
        profile.role = FlexUser.PROSUMER
        profile.save()
        return response

class SuccessView(TemplateView):
    template_name = "registration/success.html"
