from django.db import models

# Create your models here.
class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=50)
    idade = models.IntegerField()