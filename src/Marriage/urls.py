from django.urls import path
from . import views
app_name = 'Marriage'
urlpatterns = [
    path('create/', views.create_marriage, name='create_marriage'),
    path('edit/<int:marriage_id>/', views.edit_marriage, name='edit_marriage'),
    path('print/<int:marriage_id>/', views.print_marriage_certificate, name='print_marriage_certificate'),
    path('list/', views.marriage_list, name='marriage_list'),

]