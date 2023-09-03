from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import *

class signup_form(UserCreationForm):
    class Meta:
        model = account_credentials
        fields = ['username','first_name','last_name','email','csv','password1','password2']

    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'email address', 'required': 'required'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'first name', 'required': 'required'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'last name', 'required': 'required'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'username', 'required': 'required'}))

    error_messages = {
        'username': {
            'unique': ("username exists, choose another.")
        }
    }

    labels = {
        'csv': ('Your CSV file'),
    }

    def __init__(self, *args, **kwargs):
        super(signup_form, self).__init__(*args, **kwargs)
        # Making location required
        self.fields['csv'].help_text = "Upload CSV in pdf format"


    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_superuser = True
        
        if commit:
            user.save()

        return user


class CreateProjectForm(forms.ModelForm):
    class Meta:
        model = project_collections
        fields = ('title', 'date', 'category', 'keyword', 'keyword_description', 'key_aspects')

        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'Title',
                'class': 'form-control',
                'required': 'required',
            }),
            'keyword': forms.TextInput(attrs={
                'placeholder': 'Keyword',
                'class': 'form-control',
                'required': 'required',
            }),
            'keyword_description': forms.Textarea(attrs={
                'placeholder': 'Keyword Description',
                'class': 'form-control',
            }),
            'key_aspects': forms.Textarea(attrs={
                'placeholder': 'Key Aspects',
                'class': 'form-control'
            })

        }