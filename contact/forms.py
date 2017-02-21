from django import forms
from .models import Contact_db

class ContactForm(forms.ModelForm):
	class Meta:
		model = Contact_db
		fields = ['name', 'email', 'content']
		widgets = {
            'name': forms.TextInput(attrs={'class': 'myfieldclass'}),
            'email': forms.EmailInput(attrs={'class': 'myfieldclass'}),
            'content': forms.TextInput(attrs={'class': 'myfieldclass'}),
        }
