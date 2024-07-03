from django.urls import path

from .views import acts_request_page, acts_request_form

app_name = 'acts_request'
urlpatterns = [
    path('', acts_request_page, name='acts_request'),
    path('formulaire-de-demande', acts_request_form, name='acts_request_form'),
]
