from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext as _


# Create your models here.
class FlexUser(models.Model):
    ROLES=[
        ('prosumer', _('Prosumer')),
        ('aggragator', _('Agregator'))
    ]
    user = models.OneToOneField(User, related_name='user_info', on_delete=models.CASCADE)
    anonimizedId = models.CharField(max_length=50)
    role = models.CharField(max_length=10, choices=ROLES)
