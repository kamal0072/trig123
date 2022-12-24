from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm

class UserRegistrationform(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    email = forms.EmailField(max_length=50, help_text='Enter a valid email address')
    profile_pic=forms.ImageField()
    class Meta:
        model=User
        fields=['username', 'first_name', 'last_name','email', 'password1','password2',"profile_pic"]

class UserEditForm(UserChangeForm):
    password=None
    class Meta:
        model=User
        fields=['username', 'first_name', 'last_name','email']
        labels={
            "first_name":'First Name',
            "last_name":"Last Name",
            'email':"Email Address",
            }