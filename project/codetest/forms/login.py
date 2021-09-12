from django import forms

from codetest.models import User

class LoginForm(forms.Form):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email'}))
    password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Use phone number as password'}))