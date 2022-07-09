from django import forms
from .models import File

class UploadForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ['title','desc','file']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Title', 'class':'form-control'}),
            'desc': forms.TextInput(attrs={'placeholder': 'Description', 'class':'form-control'}),
        }