from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import basicCustomUser

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = basicCustomUser
        fields = ('email',)


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = basicCustomUser
        fields = ('email',)