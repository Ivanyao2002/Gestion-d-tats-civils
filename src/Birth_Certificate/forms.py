from django import forms
from Model.models import Birth


class BirthForm(forms.ModelForm):
    class Meta:
        model = Birth
        exclude = ['creation_date']


class BirthEditForm(forms.ModelForm):
    class Meta:
        model = Birth
        fields = [
            'birth_date',
            'birth_time',
            'child_last_name',
            'child_first_name',
            'birthplace',
            'father',
            'father_profession',
            'mother',
            'mother_profession'
        ]

    def __init__(self, *args, **kwargs):
        super(BirthEditForm, self).__init__(*args, **kwargs)
        self.fields['birth_date'].widget.attrs.update({'class': 'form-control'})
        self.fields['birth_time'].widget.attrs.update({'class': 'form-control'})
        self.fields['child_last_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['child_first_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['birthplace'].widget.attrs.update({'class': 'form-control'})
        self.fields['father'].widget.attrs.update({'class': 'form-control'})
        self.fields['father_profession'].widget.attrs.update({'class': 'form-control'})
        self.fields['mother'].widget.attrs.update({'class': 'form-control'})
        self.fields['mother_profession'].widget.attrs.update({'class': 'form-control'})