from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

from flexcoop_auth_server import settings
from user_management.models import FlexUser

class ProfileInline(admin.StackedInline):
    model = FlexUser
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'


def send_welcome_email(modeladmin, request, queryset):
    for user in queryset.all():
        print(user)
        context = {
            'domain': settings.SITE_URL,
            'site_name': settings.SITE_URL,
            'coop': settings.SITE_URL,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode(),
            'user': user,
            'token': default_token_generator.make_token(user),
            'protocol': 'https',
        }
        print(user.email)
        send_mail(
            "Welcome to flexcoop", render_to_string("registration/emails/welcome_user_admin.txt", context), settings.EMAIL_HOST_USER,
                [user.email], fail_silently=False)

send_welcome_email.short_description = "Send welcome email to selected users"

class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline, )
    actions = [send_welcome_email]
    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)