from django.contrib import messages
from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from .forms import ConnexionForm, UserRegistrationForm, UserUpdateForme
from Model.models import Roles, UsersAuth


# Create your views here.

class Connexion(LoginView):
    template_name = 'login.html'
    form_class = ConnexionForm

    def get_success_url(self):
        print(self.request.user.role)
        if self.request.user.role == 'ADMIN':
            return reverse('auth:list_users')
        elif self.request.user.role == 'Agent de saisir':
            return reverse('auth:registration_user')


def log_out(request):
    logout(request)
    messages.success(request, "Vous avez été déconnecté avec succès.")
    return redirect('auth:login')


def registration(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST, request.FILES)
        if user_form.is_valid():
            user_form.save()
            messages.success(request, 'Un nouvel utilisateur a été ajouté avec succès.')
            return redirect('auth:list_users')
        else:
            print(user_form.errors)
    else:
        user_form = UserRegistrationForm()

    return render(request, 'registration.html', {'user_form': user_form})


def list_users(request):
    users = UsersAuth.objects.all()  # Récupère tous les utilisateurs
    return render(request, 'users_list.html', {'users': users})


def delete_user(request, user_id):
    user = get_object_or_404(UsersAuth, pk=user_id)
    user.is_deleted = True
    user.is_active = False
    user.save()
    return redirect('auth:list_users')


def edit_user(request, user_id):
    user = get_object_or_404(UsersAuth, pk=user_id)
    if request.method == 'POST':
        form_user = UserUpdateForme(request.POST, request.FILES, instance=user)
        if form_user.is_valid():
            user = form_user.save(commit=False)
            new_file = request.FILES.get('image', None)
            if new_file:
                user.image = new_file
            user.save()
            form_user.save()
            return redirect('auth:list_users')
    else:
        form_user = UserUpdateForme(instance=user)
    return render(request, 'user_edit.html',
                  {'form_user': form_user, 'user': user})
