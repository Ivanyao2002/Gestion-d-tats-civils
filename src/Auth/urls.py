from django.urls import path

from .views import registration, Connexion, list_users, edit_user, delete_user, log_out

app_name = 'auth'
urlpatterns = [
    path('login/', Connexion.as_view(), name='login'),
    path('logout/', log_out, name='logout'),
    path('user-add/', registration, name='registration_user'),
    path('users-list/', list_users, name='list_users'),
    path('user-edit/<int:user_id>/', edit_user, name='edit_user'),
    path('user-delete/<int:user_id>/', delete_user, name='delete_user'),
]
