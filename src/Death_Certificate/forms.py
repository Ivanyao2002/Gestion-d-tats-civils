from django import forms
from Model.models import Death


class DeathForm(forms.ModelForm):
    class Meta:
        model = Death
        exclude = ['creation_date']
