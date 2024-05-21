from django import forms
from .models import System, SecurityEvent

class SystemForm(forms.ModelForm):
    class Meta:
        model = System
        fields = ['name', 'description']

class SecurityEventForm(forms.ModelForm):
    class Meta:
        model = SecurityEvent
        fields = ['system', 'event_type', 'description']
