from django.db import models

class Usuario(models.Model):

    id_usuario = models.AutoField(primary_key=True)
    nome_usuario = models.TextField(max_length=255, null=False)
    email = models.EmailField(unique=True, null=False)
    senha = models.TextField(max_length=100, null=False)

    