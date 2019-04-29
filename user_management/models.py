import uuid

from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext as _


# Create your models here.
from flexcoop_auth_server import settings


class FlexUser(models.Model):
    PROSUMER = 'prosumer'
    AGGREGATOR = 'aggregator'
    ROLES=[
        (PROSUMER, _('Prosumer')),
        (AGGREGATOR, _('Aggregator'))
    ]
    user = models.OneToOneField(User, related_name='user_info', on_delete=models.CASCADE)
    anonimizedId = models.CharField(max_length=50)
    role = models.CharField(max_length=10, choices=ROLES)

    def get_anonimizedID(self):
        self.anonimizedId = str(uuid.uuid5(uuid.UUID(settings.OAUTH_SERVER_UUID), self.user.username))