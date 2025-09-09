from django import forms
from core.models import ContactMessage

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = "__all__"
        widgets = {
            "name": forms.TextInput(attrs={
                "placeholder": "Name",
            }),
            "email": forms.EmailInput(attrs={
                "placeholder": "Email",
            }),
            "phone": forms.TextInput(attrs={
                "placeholder": "Phone",
            }),
            "message": forms.TextInput(attrs={
                "placeholder": "Message",
                "class": "message-box",
            })
        }

