from django import forms
from .models import blog
from django.contrib.auth.models import User


class blogform(forms.ModelForm):
    class Meta:
        model=blog
        fields=('bloger_about', 'bloger_pic', 'blogger_author','bloger_post')


class signupform(forms.ModelForm):
    class Meta:
        password = forms.CharField(widget=forms.PasswordInput)
        model=User
        fields=('username', 'last_name', 'first_name', 'email', 'password')
        widgets={'password':forms.PasswordInput(),}
