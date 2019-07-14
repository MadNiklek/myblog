from django import forms
from . import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django.core.exceptions import ValidationError

class CreateArticle(forms.ModelForm):
    class Meta:
        model = models.Article
        fields = ['title','body','slug','thumb']


# class RegisterUserForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ['username', 'email']
#         widgets = {
#             'username': forms.TextInput(attrs={'class': 'input', 'autofocus': True}),
#             'email': forms.EmailInput(attrs={'class': 'input', 'required': True})
#         }
#     def clean_password2(self):
#         cd = self.cleaned_data
#         if cd['password2'] != cd['password']:
#             raise ValidationError("Password don't match")
#
#         return cd['password2']
