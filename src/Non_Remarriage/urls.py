from django.urls import path
from . import views

app_name = 'Non_remarriage'
urlpatterns = [
    path('list/', views.non_remarriage_list, name='list'),
    path('create/', views.non_remarriage_create, name='create'),
    path('edit/<int:non_remarriage_id>/', views.non_remarriage_edit, name='edit'),
    path('print/<int:non_remarriage_id>/', views.non_remarriage_print, name='print'),
]