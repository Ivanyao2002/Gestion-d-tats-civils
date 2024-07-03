from django import forms

from Model.models import Request


class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(RequestForm, self).__init__(*args, **kwargs)

        self.fields['email'].error_messages = {
            'unique': 'Ce mail existe déjà.',
            'required': 'Ce champ est obligatoire.'
        }

        self.fields['phone'].error_messages = {
            'unique': 'Ce numéro de téléphone existe déjà.',
            'required': 'Ce champ est obligatoire.'
        }
