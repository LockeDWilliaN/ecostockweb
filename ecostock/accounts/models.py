from django.db import models

# Create your models here.
class Produto(models.Model):
    codigo = models.CharField(max_length=10)
    nome = models.CharField(max_length=50)
    quantidade = models.IntegerField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    
    