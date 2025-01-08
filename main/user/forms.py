from .models import User
from django.forms import ModelForm, TextInput

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'name', 'surname', 'phone_number','email']
        widgets = {
            "username":TextInput(attrs={
                'class':'form-control'
            }),
            "name": TextInput(attrs={
                'class': 'form-control'
            }),
            "surname": TextInput(attrs={
                'class': 'form-control'
            }),
            "phone_number": TextInput(attrs={
                'class': 'form-control'
            }),
            "email": TextInput(attrs={
                'class': 'form-control'
            })
        }






