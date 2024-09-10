from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class CustomerLoginForm(AuthenticationForm):
    def confirm_login_allowed(self, user):
        if not user.groups.filter(name='Customers').exists():
            raise ValidationError("This account is not allowed to log in as a customer.", code='invalid_login')

class SellerLoginForm(AuthenticationForm):
    def confirm_login_allowed(self, user):
        if not user.groups.filter(name='Sellers').exists():
            raise ValidationError("This account is not allowed to log in as a seller.", code='invalid_login')
