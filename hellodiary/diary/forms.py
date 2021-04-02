from django import forms
from .models import *

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CreateUserForm(UserCreationForm):   
    diary_name = forms.CharField(max_length=50)
    class Meta:
        model = User
        fields = ['username', 'first_name', 'email', 'password1', 'password2', 'diary_name']


class DiaryForm(forms.ModelForm):
    class Meta:
        model = Diary
        fields = ['title', 'diary_entry', 'date_created']

        widgets = {
            'title': forms.Textarea(attrs={'class': 'title-area', 'placeholder': 'Entry Title', 'autocomplete': 'off'}),
            'diary_entry': forms.Textarea(attrs={'class': 'diary-area', 'placeholder': 'Your entry here', 'autocomplete': 'off'})
        }

