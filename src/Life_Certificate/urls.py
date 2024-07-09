from django.urls import path
from .views import life_list, life_create, life_update, print_life_certificate

app_name = 'Life'
urlpatterns = [
    path('add/', life_create, name='life_create'),
    path('list/', life_list, name='life_list'),
    path('edit/<int:life_id>/', life_update, name='life_update'),
    path('print/<int:life_id>/', print_life_certificate, name='print_life_certificate'),
]
