from django.contrib import admin
from .models import Projeto, ProjetoImagens

class ProjetoImagemInline(admin.TabularInline):
    model = ProjetoImagens
    extra = 1


# Register your models here.
@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    list_display = ('titulo',)
    search_fields = ('titulo',)
    inlines = [ProjetoImagemInline]