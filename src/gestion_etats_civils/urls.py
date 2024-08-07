"""
URL configuration for gestion_etats_civils project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import accueil
from django.conf.urls.static import static
from gestion_etats_civils import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', accueil, name='index'),
    path('Extrait-de-naissance/', include('Birth_Certificate.urls')),
    path('Mariage/', include('Marriage.urls')),
    path('Settings/', include('Settings.urls')),
    path('acts-request/', include('acts_request.urls')),
    path('Certificat-de-vie/', include('Life_Certificate.urls')),
    path('Certificat-de-non-remarriage/', include('Non_Remarriage.urls')),
    path('Extrait-de-décès/', include('Death_Certificate.urls')),
    path('Users/', include('Auth.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
