# forms.py
from django import forms
from Model.models import Marriage


class MarriageForm(forms.ModelForm):
    class Meta:
        model = Marriage
        fields = [
            'registry', 'groom_first_name', 'groom_last_name', 'groom_birthplace',
            'groom_birthdate', 'groom_father', 'groom_mother', 'groom_domicile',
            'bride_first_name', 'bride_last_name', 'bride_birthplace', 'bride_birthdate',
            'bride_father', 'bride_mother', 'bride_domicile', 'date', 'hours'
        ]
