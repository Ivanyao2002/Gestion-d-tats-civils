from django.urls import path
from .views import print_death_certificate, death_list, death_create, death_update

app_name = 'Death'
urlpatterns = [
    path('add/', death_create, name='create'),
    path('list/', death_list, name='list'),
    path('edit/<int:death_id>/', death_update, name='update'),
    path('print/<int:death_id>/', print_death_certificate, name='print'),
]