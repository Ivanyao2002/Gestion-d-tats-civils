from django.shortcuts import render, get_object_or_404, redirect
from Model.models import Life, Settings
from .forms import LifeForm
from django.utils import timezone


def print_life_certificate(request, life_id):
    life = get_object_or_404(Life, id=life_id)
    date = timezone.now().strftime('%d/%m/%Y')
    heure = timezone.now().strftime("%H:%M:%S")
    annee = timezone.now().year
    settings = Settings.get_settings()
    return render(request, 'gamma.html',
                  {'life': life, 'annee': annee, 'setting': settings,
                   'date': date, 'heure': heure})


def life_list(request):
    lives = Life.objects.all()
    return render(request, 'life_list.html', {'lifes': lives})


def life_create(request):
    if request.method == 'POST':
        form = LifeForm(request.POST)
        if form.is_valid():
            life = form.save()
            return redirect('Life:print_life_certificate', life_id=life.id)
    else:
        form = LifeForm()
    return render(request, 'create_LifeCertificate.html', {'form': form})


def life_update(request, life_id):
    life = get_object_or_404(Life, pk=life_id)
    if request.method == 'POST':
        form = LifeForm(request.POST, instance=life)
        if form.is_valid():
            form.save()
            return redirect('Life:print_life_certificate', life_id=life.id)
    else:
        form = LifeForm(instance=life)
    return render(request, 'update_life.html', {'form': form, 'life': life})
