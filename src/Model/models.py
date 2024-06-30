from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.utils import timezone

class MyUserManager(BaseUserManager):
    def create_user(self, username, password=None):
        if not username:
            raise ValueError("You must provide a username")

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

class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    role = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/')
    USERNAME_FIELD = 'username'
    objects = MyUserManager()

class Registry(models.Model):
    deputies = models.CharField(max_length=100)
    annexes = models.CharField(max_length=100)
    registry_id = models.CharField(max_length=100)
    creation_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.registry_id

class Marriage(models.Model):
    registry = models.ForeignKey(Registry, on_delete=models.CASCADE)
    marriage_location = models.CharField(max_length=100)
    registration_date = models.DateField()
    groom_first_name = models.CharField(max_length=100)
    groom_last_name = models.CharField(max_length=100)
    groom_birthplace = models.CharField(max_length=100)
    groom_birthdate = models.DateField()
    groom_profession = models.CharField(max_length=100)
    groom_address = models.CharField(max_length=200)
    marriage_register = models.CharField(max_length=100)
    witness1 = models.CharField(max_length=100)
    witness2 = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='images/')
    creation_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Marriage between {self.groom_last_name} and {self.groom_first_name}'

class Death(models.Model):
    registry = models.ForeignKey(Registry, on_delete=models.CASCADE)
    death_id = models.AutoField(primary_key=True)
    declarant_age = models.IntegerField()
    declarant_main_residence = models.CharField(max_length=200)
    death_location = models.CharField(max_length=100)
    death_date = models.DateField()
    deceased_last_name = models.CharField(max_length=100)
    deceased_first_name = models.CharField(max_length=100)
    deceased_birthplace = models.CharField(max_length=100)
    deceased_birthdate = models.DateField()
    deceased_profession = models.CharField(max_length=100)
    creation_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.deceased_last_name

class Birth(models.Model):
    registry = models.ForeignKey(Registry, on_delete=models.CASCADE)
    registration_location = models.CharField(max_length=100)
    birth_date = models.DateField()
    child_last_name = models.CharField(max_length=100)
    child_first_name = models.CharField(max_length=100)
    birthplace = models.CharField(max_length=100)
    father_last_name = models.CharField(max_length=100)
    father_first_name = models.CharField(max_length=100)
    father_profession = models.CharField(max_length=100)
    father_address = models.CharField(max_length=200)
    creation_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.child_last_name

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

class Request(models.Model):
    registry = models.ForeignKey(Registry, on_delete=models.CASCADE)
    request_id = models.AutoField(primary_key=True)
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    creation_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.subject
