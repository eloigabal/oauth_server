from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, FormView

from flexcoop_auth_server import settings
from oidc_provider.lib.utils.token import client_id_from_id_token
from oidc_provider.models import Client
from user_management.forms import SignUpForm, ProfileForm

# Create your views here.
from user_management.models import FlexUser
from urllib.parse import urlsplit, parse_qs, urlencode, urlunsplit
from django.core.mail import send_mail


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
        # DEACTIVATED UNTIL DECIDED BY THE PROJECT
#        context = {"coop": settings.SITE_URL, "username": user.username, "password": form.cleaned_data['password']}
#        send_mail(
#            'New user for flexcoop',
#            render_to_string('registration/welcome_user.txt', context),
#            settings.EMAIL_HOST_USER,
#            [user.email],
#            fail_silently=False
#        )

        return response

class SuccessView(TemplateView):
    template_name = "registration/success.html"

class ProfileView(LoginRequiredMixin, FormView):
    model = User
    template_name = "registration/profile.html"
    success_url = reverse_lazy('user_management:profile')
    form_class = ProfileForm
    raise_exception = True
    def get_form(self, form_class=ProfileForm):
        id_token_hint = self.request.GET.get('id_token_hint', '')
        return_uri = self.request.GET.get('referrer_uri', '')
        state = self.request.GET.get('state', '')
        client_id = None
        if id_token_hint:
            client_id = client_id_from_id_token(id_token_hint)
            try:
                client = Client.objects.get(client_id=client_id)
                uri = urlsplit(return_uri)
                t_uri = "{uri.scheme}://{uri.netloc}".format(uri=uri)
                for c_uri_reg in client.redirect_uris:
                    c_uri_obj = urlsplit(c_uri_reg)
                    c_uri = "{uri.scheme}://{uri.netloc}".format(uri=c_uri_obj)
                    if t_uri == c_uri:
                        query_params = parse_qs(uri.query)
                        print(query_params)
                        if state:
                            query_params['state'] = state
                            uri = uri._replace(query=urlencode(query_params, doseq=True))
                            self.request.session['back_url'] = urlunsplit(uri)
                        else:
                            self.request.session['back_url'] = return_uri
                        break
            except Client.DoesNotExist:
                self.request.session['back_url'] = ""


        return form_class(instance=self.request.user, **self.get_form_kwargs())

    def form_valid(self, form):
        form.save()
        return super(ProfileView, self).form_valid(form)
