from django.urls import path
from .views import setting
app_name = 'Settings'

urlpatterns = [
    path('', setting, name='settings')
]
