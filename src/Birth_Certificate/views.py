import os
from docx import Document
from docx2pdf import convert
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.conf import settings
from .forms import BirthForm
from Model.models import Birth, Registry, Settings
from django.utils import timezone
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
import datetime


def print_birth_certificate(request, birth_record_id):
    birth_record = get_object_or_404(Birth, id=birth_record_id)
    annee = timezone.now().year
    registry_id = birth_record.registry_id
    registry = Registry.objects.get(id=registry_id)
    settings = Settings.get_settings()
    return render(request, 'beta.html',
                  {'birth_record': birth_record, 'annee': annee, 'registre': registry, 'setting': settings})


def create_birth(request):
    if request.method == 'POST':
        form = BirthForm(request.POST)
        if form.is_valid():
            birth_record = form.save(commit=False)
            birth_record.creation_date = timezone.now()
            birth_record.save()
            messages.success(request, 'Extrait de naissance créé avec succès.')
            # return generate_birth_certificate_pdf(birth_record)
            # return redirect(reverse('print_birth_certificate', birth_record_id=birth_record.id))  # Assurez-vous que cette URL existe

            # Stocker birth_record dans la session
            form = BirthForm()

            # Rediriger vers une autre vue qui utilisera beta.html
            return redirect('Birth_Certificate:print_birth_certificate', birth_record_id=birth_record.id)
        else:
            for field in form:
                for error in field.errors:
                    print(f"Error in {field.name}: {error}")
            print(form.errors)
    else:
        form = BirthForm()

    registries = Registry.objects.all()
    return render(request, 'Create_birthCertificate.html',
                  {'form': form, 'registries': registries, })

# def generate_birth_certificate_pdf(birth):
#     try:
#         # Charger le modèle de document
#         template_path = os.path.join(settings.BASE_DIR, 'extrait.docx')
#         doc = Document(template_path)
#
#         # Remplir le modèle avec les données du formulaire
#         for p in doc.paragraphs:
#             if 'Est né' in p.text:
#                 p.text = f"Est né {birth.child_first_name} {birth.child_last_name}."
#             if 'INFORMATICIEN' in p.text:
#                 p.text = p.text.replace('INFORMATICIEN', f'{birth.father_profession}')
#             # Ajouter d'autres remplacements pour d'autres champs ici
#
#         # Enregistrer le document rempli
#         output_path = os.path.join(settings.BASE_DIR, 'extrait_filled.docx')
#         doc.save(output_path)
#
#         # Convertir en PDF
#         convert(output_path, output_path.replace('.docx', '.pdf'))
#
#         # Retourner le fichier PDF en réponse HTTP
#         pdf_path = output_path.replace('.docx', '.pdf')
#         with open(pdf_path, 'rb') as pdf_file:
#             response = HttpResponse(pdf_file.read(), content_type='application/pdf')
#             response[
#                 'Content-Disposition'] = f'inline; filename="Extrait_de_naissance_{birth.child_last_name}_{birth.child_first_name}.pdf"'
#             return response
#
#     except Exception as e:
#         # Gérer les erreurs
#         print(f"Erreur lors de la génération du PDF : {e}")
#         return HttpResponse('Erreur lors de la génération du PDF', status=500)
