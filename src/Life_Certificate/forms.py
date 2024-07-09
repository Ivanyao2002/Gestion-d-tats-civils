from django import forms
from Model.models import Life


class LifeForm(forms.ModelForm):
    class Meta:
        model = Life
        fields = ['name', 'surname', 'job', 'birthdate', 'birthplace']
