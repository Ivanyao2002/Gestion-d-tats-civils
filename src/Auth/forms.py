from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm

from Model.models import UsersAuth
from django import forms


class ConnexionForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(ConnexionForm, self).__init__(*args, **kwargs)

        self.fields['username'].error_messages = {
            'required': "Veuillez saisir un Nom d'utilisateur valide !!"
        }
        self.fields['password'].error_messages = {
            'required': "Veuillez saisir un mot de passe valide !!"
        }
        self.error_messages = {
            "invalid_login":
                "Veuillez saisir les mêmes informations que lors de la création de votre compte. "
                "Vous devez respecter les majuscules ou les minuscules !!",
            "inactive": "Ce compte est inactif veuillez contacter votre administrateur."
        }

    class Meta:
        model = UsersAuth
        fields = 'username', 'password'


class UserRegistrationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)

        self.fields['username'].error_messages = {
            'unique': 'Ce nom d\'utilisateur existe déjà.',
            'required': 'Ce champ est obligatoire.'
        }

        self.fields['email'].error_messages = {
            'unique': 'Cet email existe déjà.',
            'required': 'Ce champ est obligatoire.'
        }

    class Meta:
        model = UsersAuth
        fields = ('username', 'first_name', 'last_name', 'phone', 'email', 'role', 'image',)


class UserUpdateForme(UserChangeForm):
    class Meta:
        model = UsersAuth
        fields = ('username', 'first_name', 'last_name', 'phone', 'email', 'role', 'image',)
