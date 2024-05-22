from django import forms
from .models import System, SecurityEvent
# forms.py

from django import forms
from .models import Copyright

from .models import Atack

class AtackForm(forms.ModelForm):
    class Meta:
        model = Atack
        fields = ['author', 'title', 'description']

class CopyrightForm(forms.ModelForm):
    class Meta:
        model = Copyright
        fields = ['watermark','author', 'title', 'year']

class SystemForm(forms.ModelForm):
    class Meta:
        model = System
        fields = ['name', 'description']

class SecurityEventForm(forms.ModelForm):
    class Meta:
        model = SecurityEvent
        fields = ['system', 'event_type', 'description']
