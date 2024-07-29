from django.contrib import admin

# Register your models here.
from Model.models import Roles, UsersAuth


@admin.register(Roles)
class RolesAdmin(admin.ModelAdmin):
    list_display = ('id', 'role')  # Champs à afficher dans la liste
    search_fields = ('role',)  # Champs à rechercher
