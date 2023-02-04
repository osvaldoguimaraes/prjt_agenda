from django.contrib import admin
from .models import Categoria, Contato

# Register your models here.

# Aqui serve para mostrar todos os campos do meu admin no django
class ContatoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'sobrenome', 'email', 'telefone', 'categoria', 'mostrar' )
    list_display_links = ('id', 'nome', 'sobrenome')
    list_filter = ('nome', 'sobrenome')
    list_per_page = 10
    search_fields = ('nome', 'sobrenome', 'telefone')
    list_editable = ('telefone', 'mostrar')

admin.site.register(Categoria)
admin.site.register(Contato, ContatoAdmin)