from django.shortcuts import render, redirect
from .forms import RequestForm
from django.contrib import messages
from django.http import JsonResponse


# Create your views here.

def acts_request_page(request):
    return render(request, 'external/index.html')


def acts_request_form(request):
    if request.method == 'POST':
        request_form = RequestForm(request.POST, request.FILES)
        if request_form.is_valid():
            request_form.save()
            request_form = RequestForm()
            print("request_form")
            messages.success(request, 'Votre demande a été envoyée avec succès.')
            return JsonResponse({'success': True})

        else:
            print(request_form.errors)
    else:
        request_form = RequestForm()
    return render(request, 'external/index.html', {'request_form': request_form})
# return redirect('acts_request:acts_request')
