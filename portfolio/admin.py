from django.contrib import admin
from .models import Projeto

# Register your models here.
@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'data_criacao')
    search_fields = ('titulo',)
    list_filter = ('data_criacao',)