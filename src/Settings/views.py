from django.shortcuts import render, redirect
from Model.models import Settings
from .forms import SettingsForm  # Assurez-vous d'avoir un formulaire correspondant


def setting(request):
    # Récupérer les paramètres existants depuis la base de données
    settings = Settings.get_settings()

    if request.method == 'POST':
        # Créer une instance de formulaire avec les données postées
        form = SettingsForm(request.POST, request.FILES, instance=settings)

        if form.is_valid():
            form.save()  # Sauvegarder les données mises à jour dans la base de données
            return redirect('Settings:settings')  # Rediriger vers la même page pour rafraîchir les données
    else:
        form = SettingsForm(instance=settings)  # Pré-remplir le formulaire avec les données existantes

    return render(request, 'settings.html', {'settings': settings, 'form': form})