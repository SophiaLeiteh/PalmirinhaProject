from django.contrib import admin
from ReceitaApp.models import Receita
from ReceitaApp.models import Categoria

# Register your models here.
class ReceitaAdmin (admin.ModelAdmin):
    #colunas exibidas
    list_display = ['nome', 'ingredientes', 'modo_de_preparo', 'grau_de_dificuldade']
    #colunas com link para editar
    list_display_links = ['nome', 'ingredientes']
    #colunas para filtro
    list_filter = ['nome']
    
class CategoriaAdmin(admin.ModelAdmin):
     list_display = ['nome']
     list_display = ['nome']
     search_fields = ['nome']

admin.site.register(Receita,ReceitaAdmin)
admin.site.register(Categoria,CategoriaAdmin)