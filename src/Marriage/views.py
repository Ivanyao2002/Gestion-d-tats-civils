# views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .forms import MarriageForm
from Model.models import Marriage, Registry, Settings
from django.utils import timezone


def print_marriage_certificate(request, marriage_id):
    marriage_record = get_object_or_404(Marriage, id=marriage_id)
    date = timezone.now().strftime('%d/%m/%Y')
    heure = timezone.now().strftime("%H:%M:%S")
    annee = timezone.now().year
    registry_id = marriage_record.registry_id
    registry = Registry.objects.get(id=registry_id)
    settings = Settings.get_settings()
    return render(request, 'alpha.html',
                  {'marriage_record': marriage_record, 'annee': annee, 'registre': registry, 'setting': settings,
                   'date': date, 'heure': heure})


def create_marriage(request):
    if request.method == 'POST':
        form = MarriageForm(request.POST)
        if form.is_valid():
            marriage = form.save()
            return redirect('Marriage:print_marriage_certificate', marriage_id=marriage.id)
    else:
        form = MarriageForm()

    registries = Registry.objects.all()
    return render(request, 'create_marriage.html', {'form': form, 'registries': registries})


def edit_marriage(request, marriage_id):
    marriage = get_object_or_404(Marriage, pk=marriage_id)
    if request.method == 'POST':
        form = MarriageForm(request.POST, instance=marriage)
        if form.is_valid():
            form.save()
            return redirect('Marriage:print_marriage_certificate', marriage_id=marriage.id)
    else:
        form = MarriageForm(instance=marriage)

    return render(request, 'edit_marriage.html', {'form': form, 'marriage': marriage})


def marriage_list(request):
    marriages = Marriage.objects.all()
    return render(request, 'List_marriage.html', {'marriages': marriages})
