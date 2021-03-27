from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CreateUserForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=200)
    diary_name = forms.CharField(max_length=200)
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'email', 'password1', 'password2', 'diary_name']

        widgets = {
            'first_name': forms.TextInput(
                attrs={'placeholder': 'Enter title here',
                'cols': 400, 'rows': 30, 'style':'border:0; font-size:20px'})
        }
