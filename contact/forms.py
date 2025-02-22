from django import forms
from .models import ContactMessage


class ContactForm(forms.ModelForm):
    """
    Form for creating contact messages
    Based on the ContactMessage model

    Fields:
        - name (CharField)
        - email (EmailField)
        - interest_to_join (BooleanField)
        - message (TextField)
    """
    class Meta:
        model = ContactMessage
        fields = ('name', 'email', 'interest_to_join', 'message')
        widgets = {
            'name': forms.TextInput(attrs={'autocomplete': 'name'}),
            'email': forms.EmailInput(attrs={'autocomplete': 'email'}),
        }
