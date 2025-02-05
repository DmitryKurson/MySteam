from user.models import Game
from django.forms import ModelForm, TextInput, NumberInput

class GameForm(ModelForm):
    class Meta:
        model = Game
        fields = ['title', 'genre', 'description', 'price','languages']
        widgets = {
            "title":TextInput(attrs={
                'class':'form-control'
            }),
            "genre": TextInput(attrs={
                'class': 'form-control'
            }),
            "description": TextInput(attrs={
                'class': 'form-control'
            }),
            "price": NumberInput(attrs={
                'class': 'form-control'
            }),
            "languages": TextInput(attrs={
                'class': 'form-control'
            })
        }






