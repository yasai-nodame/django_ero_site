from django import forms 
from .models import Ero_title 

class TitleForm(forms.ModelForm):
    class Meta:
        model = Ero_title 
        fields = ['title']
        widgets = {
            'title' : forms.TextInput(attrs={'placeholder':'キーワードを入力','class':'input-field'})
        }
        