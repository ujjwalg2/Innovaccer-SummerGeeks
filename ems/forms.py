from django import forms
from .models import *

class UserForm(forms.ModelForm):
    firstname = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'First Name', 'required':'true'}))
    lastname = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Last Name', 'required':'true'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Email', 'required':'true'}))
    contact = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Contact', 'required':'true'}))

    class Meta:
        model = User
        fields = ['firstname', 'lastname', 'email', 'contact']