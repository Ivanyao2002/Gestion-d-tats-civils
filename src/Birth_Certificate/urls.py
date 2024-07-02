from django.urls import path

from Birth_Certificate.views import create_birth

app_name = 'Birth_Certificate'
urlpatterns = [
    path('Creation_extrait/', create_birth, name='Creation_extrait'),
]
