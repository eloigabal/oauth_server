from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, FormView

from oidc_provider.models import Client
from user_management.forms import SignUpForm, ProfileForm

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

class ProfileView(FormView):
    model = User
    template_name = "registration/profile.html"
    success_url = reverse_lazy('user_management:profile')
    form_class = ProfileForm

    def get_form(self, form_class=ProfileForm):
        return form_class(instance=self.request.user, **self.get_form_kwargs())

    def form_valid(self, form):
        form.save()
        return super(ProfileView, self).form_valid(form)

    def get_back_url(self):
        params = self.request.GET
        if 'referrer' in params and 'referrer_uri' in params:
            client = Client.objects.get(client_id=params['referrer'])
            if params['referrer_uri'] in client.redirect_uris:
                return params['referrer_uri']
        return ""