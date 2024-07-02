from django import forms
from Model.models import Birth


class BirthForm(forms.ModelForm):
    class Meta:
        model = Birth
        exclude = ['creation_date']
