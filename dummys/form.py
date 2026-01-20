from django import forms
from tinymce.widgets import TinyMCE

from core.form import TINYMCE_BASIC_CONFIG
from dummys.models import (Dummy)


class DummyAdminForm(forms.ModelForm):
    class Meta:
        model = Dummy
        fields = "__all__"
        widgets = {
            "content": TinyMCE(mce_attrs=TINYMCE_BASIC_CONFIG),
        }
        help_texts = {
            'name': 'Enter the full legal or professional name of the dummy.',
            'image': 'Upload a professional headshot. Recommended size: 500x500px.',
            'is_hidden': 'Hide this dummy from the public listing (useful for drafts).',
        }
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            # Optional: You can also style the help text or inputs here
            self.fields['email'].widget.attrs.update({'placeholder': 'example@domain.com'})

