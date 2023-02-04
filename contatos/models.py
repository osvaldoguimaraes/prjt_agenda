from django.db import models
from django.utils import timezone

'''
CONTATOS
id: INT (automático)
nome: STR * (obrigatório)
sobrenome: STR (opcional)
telefone: STR * (obrigatório)
email: STR (opcional)
data_criacao: DATETIME (automático)
descricao: texto
categoria: CATEGORIA (outro model)

 CATEGORIA
 id: INT
 nome: STR * (obrigatório)
'''

# Create your models here.
class Categoria(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome
    
class Contato(models.Model): # Escrever models.Model é herança pois Model está herdando da classe models
    nome = models.CharField(max_length=255)
    sobrenome = models.CharField(max_length=255, blank=True)
    telefone = models.CharField(max_length=255)
    email = models.CharField(max_length=255, blank=True)
    data_criacao = models.DateTimeField(default=timezone.now)
    decricao = models.TextField(blank=True) 
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    mostrar = models.BooleanField(default = True) 

    def __str__(self):
        return self.nome
