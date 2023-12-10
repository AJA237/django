from django import forms
from .models import UserModel

# creating myy forms
class UserForm(forms.Model):
    class Meta:
        model = UserModel
        field = __all__
        