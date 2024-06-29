from django.db import models

class Utilisateur(models.Model):
    nom_user = models.CharField(max_length=100)
    prenom_user = models.CharField(max_length=100)
    telephone = models.CharField(max_length=20)
    email = models.EmailField()
    role = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/')

class Mariage(models.Model):
    lieu_mariage = models.CharField(max_length=100)
    date_enregistrement = models.DateField()
    prenom_epoux = models.CharField(max_length=100)
    nom_epoux = models.CharField(max_length=100)
    lieu_naissance_epoux = models.CharField(max_length=100)
    date_naissance_epoux = models.DateField()
    profession_epoux = models.CharField(max_length=100)
    adresse_epoux = models.CharField(max_length=200)
    registre_mariage = models.CharField(max_length=100)
    temoin1 = models.CharField(max_length=100)
    temoin2 = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='images/')
    def __str__(self):
        return f'Mariage entre {self.nom_epoux} et {self.prenom_epoux}'

class Deces(models.Model):
    id_deces = models.AutoField(primary_key=True)
    age_declarant = models.IntegerField()
    residence_principal_declarant = models.CharField(max_length=200)
    lieu_deces = models.CharField(max_length=100)
    date_deces = models.DateField()
    nom_defunt = models.CharField(max_length=100)
    prenom_defunt = models.CharField(max_length=100)
    lieu_naissance_defunt = models.CharField(max_length=100)
    date_naissance_defunt = models.DateField()
    profession_defunt = models.CharField(max_length=100)
    def __str__(self):
        return self.nom_defunt

class Naissance(models.Model):
    lieu_enregistrement = models.CharField(max_length=100)
    date_naissance = models.DateField()
    nom_enfant = models.CharField(max_length=100)
    prenom_enfant = models.CharField(max_length=100)
    lieu_naissance = models.CharField(max_length=100)
    nom_pere = models.CharField(max_length=100)
    prenom_pere = models.CharField(max_length=100)
    profession_pere = models.CharField(max_length=100)
    adresse_pere = models.CharField(max_length=200)
    def __str__(self):
        return self.nom_enfant

class Divorce(models.Model):
    lieu_jugement = models.CharField(max_length=100)
    date_jugement = models.DateField()
    nom_epoux = models.CharField(max_length=100)
    prenom_epoux = models.CharField(max_length=100)
    lieu_naissance_epoux = models.CharField(max_length=100)
    date_naissance_epoux = models.DateField()
    nom_epouse = models.CharField(max_length=100)
    prenom_epouse = models.CharField(max_length=100)
    lieu_naissance_epouse = models.CharField(max_length=100)
    date_naissance_epouse = models.DateField()
    def __str__(self):
        return f'Divorce entre {self.nom_epoux} et {self.prenom_epoux}'

class Message(models.Model):
    id_destinataire = models.ForeignKey(Utilisateur, related_name='destinataire', on_delete=models.CASCADE)
    id_auteur = models.ForeignKey(Utilisateur, related_name='auteur', on_delete=models.CASCADE)
    titre = models.CharField(max_length=200)
    texte = models.TextField()
    def __str__(self):
        return self.titre

class Demande(models.Model):
    id_demande = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    telephone = models.CharField(max_length=20)
    email = models.EmailField()
    objet = models.CharField(max_length=200)
    message = models.TextField()
    def __str__(self):
        return self.objet

class Registre(models.Model):
    adjoints = models.CharField(max_length=100)
    annexes = models.CharField(max_length=100)
    id_registre = models.CharField(max_length=100)
    def __str__(self):
        return self.id_registre

class FormationSanitaire(models.Model):
    id_formation = models.AutoField(primary_key=True)
    code_formation = models.CharField(max_length=100)
    libelle_formation = models.CharField(max_length=200)
    type_formation = models.CharField(max_length=100)
    def __str__(self):
        return self.libelle_formation
