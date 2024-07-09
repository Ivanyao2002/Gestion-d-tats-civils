from django.shortcuts import render, get_object_or_404, redirect
from Model.models import Non_remarriage, Settings
from .forms import NonRemarriageForm
from django.utils import timezone


def non_remarriage_print(request, non_remarriage_id):
    remarriage = get_object_or_404(Non_remarriage, id=non_remarriage_id)
    date = timezone.now().strftime('%d/%m/%Y')
    heure = timezone.now().strftime("%H:%M:%S")
    annee = timezone.now().year
    settings = Settings.get_settings()
    return render(request, 'delta.html',
                  {'remarriage': remarriage, 'annee': annee, 'setting': settings,
                   'date': date, 'heure': heure})


def non_remarriage_list(request):
    non_remarriages = Non_remarriage.objects.all()
    return render(request, 'non_remarriage_list.html', {'non_remarriages': non_remarriages})


def non_remarriage_create(request):
    if request.method == 'POST':

        form = NonRemarriageForm(request.POST)
        if form.is_valid():
            remarriage = form.save()
            return redirect('Non_remarriage:print', non_remarriage_id=remarriage.id)
    else:
        form = NonRemarriageForm()
    return render(request, 'create_non_remarriage.html', {'form': form})


def non_remarriage_edit(request, non_remarriage_id):
    non_remarriage = get_object_or_404(Non_remarriage, pk=non_remarriage_id)
    if request.method == 'POST':
        form = NonRemarriageForm(request.POST, instance=non_remarriage)
        if form.is_valid():
            form.save()
            return redirect('Non_remarriage:print', non_remarriage_id=non_remarriage.id)
    else:
        form = NonRemarriageForm(instance=non_remarriage)
    return render(request, 'edit_non_remarriage.html', {'form': form, 'non_remarriage': non_remarriage})
