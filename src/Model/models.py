from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class MyUserManager(BaseUserManager):
    def create_user(self, username, password=None):
        if not username:
            raise ValueError("Vous devez entrer un nom d'utilisateur !")
        if password is None:
            raise ValueError("Vous devez entrer un mot de passe !")

        user = self.model(username=username)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, password=None):
        user = self.create_user(username=username, password=password)
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user


class Roles(models.Model):
    admin = 'admin'
    civil_servant = "civil_servant"
    input_agent = 'input_agent'

    ROLE_CHOICES = [
        (admin, 'ADMIN'),
        (civil_servant, "Officier d'état civil"),
        (input_agent, "Agent de saisir"),
    ]
    role = models.CharField(max_length=100, choices=ROLE_CHOICES, default='input_agent')

    def __str__(self):
        return dict(self.ROLE_CHOICES).get(self.role, self.role)


class UsersAuth(AbstractBaseUser):
    date_mise_a_jour = models.DateTimeField(verbose_name="Date de mise a jour", auto_now=True)
    username = models.CharField(unique=True, max_length=50)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(unique=True, max_length=20)
    email = models.EmailField(unique=True, max_length=200)
    role = models.ForeignKey(Roles, on_delete=models.SET_NULL, null=True, blank=True, related_name='users')
    image = models.ImageField(upload_to='images_users/')
    is_deleted = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    USERNAME_FIELD = 'username'
    objects = MyUserManager()

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Registry(models.Model):
    deputies = models.CharField(max_length=100, null=True)
    annexes = models.CharField(max_length=100, null=True)
    registry_id = models.CharField(max_length=100)
    creation_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.registry_id


class Marriage(models.Model):
    registry = models.ForeignKey(Registry, on_delete=models.CASCADE)
    groom_first_name = models.CharField(max_length=100)
    groom_last_name = models.CharField(max_length=100)
    groom_birthplace = models.CharField(max_length=100)
    groom_birthdate = models.DateField()
    groom_father = models.CharField(max_length=100)
    groom_mother = models.CharField(max_length=200)
    groom_domicile = models.CharField(max_length=200)
    bride_first_name = models.CharField(max_length=100)
    bride_last_name = models.CharField(max_length=100)
    bride_birthplace = models.CharField(max_length=100)
    bride_birthdate = models.DateField()
    bride_father = models.CharField(max_length=100)
    bride_mother = models.CharField(max_length=200)
    bride_domicile = models.CharField(max_length=200)
    date = models.DateField()
    hours = models.TimeField()
    creation_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Marriage between {self.groom_last_name}  {self.groom_first_name} and  {self.bride_last_name}  {self.bride_first_name}'


class Death(models.Model):
    num_registry = models.CharField(max_length=20)
    registration_date = models.DateField()
    death_location = models.CharField(max_length=100, null=True)
    death_date = models.DateField(null=True)
    death_time = models.TimeField(blank=True, null=True)
    deceased_last_name = models.CharField(max_length=100, null=True)
    deceased_first_name = models.CharField(max_length=100, null=True)
    deceased_birthplace = models.CharField(max_length=100, null=True)
    deceased_birthdate = models.DateField(blank=True, null=True)
    deceased_profession = models.CharField(max_length=100, null=True)
    deceased_father = models.CharField(max_length=100, null=True)
    deceased_mother = models.CharField(max_length=100, null=True)
    creation_date = models.DateTimeField(default=timezone.now)
    registry = models.CharField(max_length=30, unique=True, blank=True, null=True)
    sexe = models.CharField(max_length=10, null=True)

    def save(self, *args, **kwargs):
        # Update the registry field before saving
        self.registry = f"{self.num_registry}-{self.registration_date.strftime('%Y%m%d')}"

        # Ensure that the registry is unique
        if Death.objects.exclude(pk=self.pk).filter(registry=self.registry).exists():
            raise ValidationError(_('A record with this registry already exists.'))

        super().save(*args, **kwargs)

    def __str__(self):
        return self.registry


class Birth(models.Model):
    num_registry = models.CharField(max_length=20)
    registration_date = models.DateField()
    birth_date = models.DateField(null=True)
    birth_time = models.TimeField(blank=True, null=True)
    child_last_name = models.CharField(max_length=100)
    child_first_name = models.CharField(max_length=100)
    birthplace = models.CharField(max_length=100, null=True)
    father = models.CharField(max_length=100, blank=True, null=True)
    mother = models.CharField(max_length=100, blank=True, null=True)
    father_profession = models.CharField(max_length=100, blank=True, null=True)
    mother_profession = models.CharField(max_length=200, blank=True, null=True)
    creation_date = models.DateTimeField(default=timezone.now)
    registry = models.CharField(max_length=30, unique=True, blank=True, null=True)
    sexe = models.CharField(max_length=10, null=True)


    def save(self, *args, **kwargs):
        # Update the registry field before saving
        self.registry = f"{self.num_registry}-{self.registration_date.strftime('%Y%m%d')}"

        # Ensure that the registry is unique
        if Birth.objects.exclude(pk=self.pk).filter(registry=self.registry).exists():
            raise ValidationError(_('A record with this registry already exists.'))

        super().save(*args, **kwargs)

    def __str__(self):
        return self.registry


class Divorce(models.Model):
    registry = models.ForeignKey(Registry, on_delete=models.CASCADE)
    court_location = models.CharField(max_length=100)
    court_date = models.DateField()
    husband_last_name = models.CharField(max_length=100)
    husband_first_name = models.CharField(max_length=100)
    husband_birthplace = models.CharField(max_length=100)
    husband_birthdate = models.DateField()
    wife_last_name = models.CharField(max_length=100)
    wife_first_name = models.CharField(max_length=100)
    wife_birthplace = models.CharField(max_length=100)
    wife_birthdate = models.DateField()
    creation_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Divorce between {self.husband_last_name} and {self.husband_first_name}'


class Life(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=100)
    job = models.CharField(max_length=100)
    birthdate = models.DateField()
    birthplace = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name} {self.surname}'


class Non_remarriage(models.Model):
    name = models.CharField(max_length=100)
    witness1 = models.CharField(max_length=100)
    witness2 = models.CharField(max_length=100)
    titre_witness1 = models.CharField(max_length=100)
    titre_witness2 = models.CharField(max_length=100)
    etat = models.CharField(max_length=100)

    def __str__(self):
        return f' le certificat de non-remariage de {self.name}'


class Request(models.Model):
    request_id = models.AutoField(primary_key=True)
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    message = models.TextField()
    file = models.FileField(upload_to='Fichier_demande/')
    creation_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.message


class Settings(models.Model):
    departement = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    commune = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='logos/')

    # Méthode pour assurer qu'il n'y a qu'une seule instance
    @classmethod
    def get_settings(cls):
        # Renvoyer toujours la première instance, ou créer une nouvelle si aucune n'existe
        settings, created = cls.objects.get_or_create(pk=1)
        return settings

    def save(self, *args, **kwargs):
        # Écraser la première instance à chaque sauvegarde
        self.pk = 1
        super(Settings, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        # Empêcher la suppression de l'instance unique
        pass
