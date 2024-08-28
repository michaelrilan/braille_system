from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *


class account_reg(UserCreationForm):
    class Meta:
        model = User
        fields = ['last_name','first_name','middlename','email','username','password1', 'password2']