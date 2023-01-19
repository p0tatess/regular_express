from django import forms

class UserForm(forms.Form):
    line = forms.CharField(max_length=255)
    regular_express = forms.CharField(max_length=255)

