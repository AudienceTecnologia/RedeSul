from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.fields.files import FileField

NIVEL_ACESSO = [
    ('Superior', 'Superior'),
    ('Administrativo', 'Administrativo'),
    ('Representante', 'Representante'),
]

class User(AbstractUser):
    Avatar = FileField(blank=True, null=True)
    Nivel_Acesso = models.CharField(max_length=255, choices=NIVEL_ACESSO, blank=True, null=True)
    CNPJ = models.CharField(max_length=255, blank=True, null=True)
    Status = models.CharField(max_length=255, blank=True, null=True)