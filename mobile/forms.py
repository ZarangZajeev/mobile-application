from django import forms
from mobile.models import Mobiles
from django.contrib.auth.models import User

class MobileForm(forms.ModelForm):
    class Meta:
        model=Mobiles
        fields="__all__"

        widgets={
            "name":forms.TextInput(attrs={"class":"form-control","placeholder":"Name"}),
            "price":forms.NumberInput(attrs={"class":"form-control","placeholder":"Price"}),
            "brand":forms.TextInput(attrs={"class":"form-control","placeholder":"Brand"}),
            "specs":forms.TextInput(attrs={"class":"form-control","placeholder":"Specs"}),
            "display":forms.TextInput(attrs={"class":"form-control","placeholder":"Display"})
        }

class RegistrationForm(forms.ModelForm):
    class Meta:
        model=User
        fields=["first_name","last_name","username","email","password"]

        widgets={
            "first_name":forms.TextInput(attrs={"class":"form-control","placeholder":"Enter First Name"}),
            "last_name":forms.TextInput(attrs={"class":"form-control","placeholder":"Enter Last Name"}),
            "username":forms.TextInput(attrs={"class":"form-control","placeholder":"Enter user name"}),
            "email":forms.EmailInput(attrs={"class":"form-control","placeholder":"Enter your Email"}),
            "password":forms.PasswordInput(attrs={"class":"form-control","placeholder":"Enter a Password"}),
        }

class LoginForm(forms.Form):
    username=forms.CharField(widget=(forms.TextInput)(attrs={"class":"form-control","placeholder":"Enter username"}))
    password=forms.CharField(widget=(forms.PasswordInput)(attrs={"class":"form-control","placeholder":"Enter Password"}))