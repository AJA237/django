from django import forms
from .models import UserModel

# creating myy forms
class UserForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields ='__all__'
        