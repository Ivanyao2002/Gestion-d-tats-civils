from django import forms
from Model.models import Non_remarriage


class NonRemarriageForm(forms.ModelForm):
    class Meta:
        model = Non_remarriage
        fields = ['name', 'witness1', 'witness2', 'etat', 'titre_witness1', 'titre_witness2']
