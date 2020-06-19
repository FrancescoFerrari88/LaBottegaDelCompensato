from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

from .managers import CustomUserManager
from taggit.managers import TaggableManager


class basicCustomUser(AbstractUser):
    '''
    This class specifies a minimal user, where only email is required and saved to the database
    '''
    username = None
    email = models.EmailField(_('email address'), unique=True, blank=False, null=False)
    is_active = models.BooleanField( _('active'), default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

class homeSection(models.Model):
    title = models.CharField(max_length=50)
    section_content = models.TextField()

    def __str__(self):
        return self.title


class Event(models.Model):
    date = models.DateTimeField(null=False, blank=False)
    place = models.CharField(max_length=50, null=False, blank=False) 
    name = models.CharField(max_length=300, null=False, blank=False)
    info = models.TextField()
    is_active = models.BooleanField(default=True)

    tags = TaggableManager()

    class Meta:
        ordering=('-date',)

    def __str__(self):
        return self.name




