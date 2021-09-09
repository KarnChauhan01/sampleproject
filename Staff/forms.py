from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Role, User

class CustomerRegister(UserCreationForm):
    role = forms.ModelChoiceField(queryset=Role.objects.all(),empty_label='select role')
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    address = forms.CharField(max_length=300)
    phone_number = forms.CharField(max_length=10)

    class Meta:
        model = User
        fields = (
            'role','username','first_name','last_name','address','phone_number','password1','password2'
        )
    