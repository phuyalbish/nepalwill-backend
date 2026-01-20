from django import forms

from contacts.models import Contact
from core.form import TINYMCE_SMALL_CONFIG




class ContactAdminForm(forms.ModelForm):
    class Meta:
        model: Contact
        fields = "__all__"

