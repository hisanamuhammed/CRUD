from django import forms
from .models import  UserProfile


class StudentRegistration(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['username', 'name', 'email']
        widgets = {
            'username' : forms.TextInput(attrs={'class' : 'form-control col-3'}),
            'name' : forms.TextInput(attrs={'class' : 'form-control col-3'}),
            'email' : forms.TextInput(attrs={'class' : 'form-control col-3'}),
            
        }