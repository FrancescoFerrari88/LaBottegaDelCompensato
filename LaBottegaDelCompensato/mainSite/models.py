from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

from .managers import CustomUserManager

class basicCustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True, blank=False, null=False)
    is_active = models.BooleanField( _('active'), default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

# Create your models here.
