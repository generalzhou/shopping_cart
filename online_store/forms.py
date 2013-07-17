from django import forms
from django.core.exceptions import ValidationError
from django.forms.models import inlineformset_factory

from online_store.models import *

class SignupForm(forms.Form):
  
  username = forms.CharField("Username", required=True)
  email = forms.EmailField( "Email", required=True )
  password = forms.CharField(widget=forms.PasswordInput(), required=True)
  confirm_password = forms.CharField(widget=forms.PasswordInput(), required=True)
  
  def clean(self):

    if (self.cleaned_data.get('password') != self.cleaned_data.get('confirm_password')):
      raise ValidationError('Passwords must match!')

    return self.cleaned_data  
