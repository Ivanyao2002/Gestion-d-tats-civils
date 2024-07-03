from django.urls import path

from .views import create_birth, print_birth_certificate

app_name = 'Birth_Certificate'
urlpatterns = [
    path('Creation_extrait/', create_birth, name='Creation_extrait'),
    path('print-birth-certificate/<int:birth_record_id>/', print_birth_certificate, name='print_birth_certificate'),

]
