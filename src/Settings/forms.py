from django import forms
from Model.models import Settings


class SettingsForm(forms.ModelForm):
    class Meta:
        model = Settings
        fields = ['city', 'commune', 'logo', 'departement']
