from django.shortcuts import render, get_object_or_404, redirect
from Model.models import Death, Registry, Settings
from .forms import DeathForm
from django.utils import timezone


def print_death_certificate(request, death_id):
    death = get_object_or_404(Death, id=death_id)
    date = timezone.now().strftime('%d/%m/%Y')
    heure = timezone.now().strftime("%H:%M:%S")
    annee = timezone.now().year
    settings = Settings.get_settings()
    registry_id = death.registry_id
    registry = Registry.objects.get(id=registry_id)
    return render(request, 'epsilon.html',
                  {'death': death, 'registre': registry, 'annee': annee, 'setting': settings,
                   'date': date, 'heure': heure})


def death_list(request):
    deaths = Death.objects.all()
    return render(request, 'death_list.html', {'deaths': deaths})


def death_create(request):
    if request.method == 'POST':
        form = DeathForm(request.POST)
        if form.is_valid():
            death = form.save()
            return redirect('Death:print', death_id=death.id)
    else:
        form = DeathForm()
    registries = Registry.objects.all()
    return render(request, 'create_death.html', {'form': form, 'registries': registries})


def death_update(request, death_id):
    death = get_object_or_404(Death, pk=death_id)
    if request.method == 'POST':
        form = DeathForm(request.POST, instance=death)
        if form.is_valid():
            form.save()
            return redirect('Death:print', death_id=death.id)
    else:
        form = DeathForm(instance=death)
    return render(request, 'update_death.html', {'form': form, 'death':death})
