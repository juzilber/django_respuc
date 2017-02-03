from django.contrib import admin
from models import *
from django.db import models
from django import forms

class VoluntarioAdmin(admin.ModelAdmin):
    search_fields = ('matricula',)
    fieldsets = [('Identificacao', {'fields': ['nome', 'data_de_nascimento', 'nome_do_curso', 'periodo', 'matricula', 'telefone_fixo', 'celular', 'email', 'idioma', 'CPF', 'genero']}), ('Endereco', {'fields': ['rua', 'numero', 'complemento', 'bairro', 'cidade', 'estado', 'CEP']})]

class ParceiroInternoInline(admin.StackedInline):
	model = ParceiroInterno
	extra = 0

class ParceiroExternoInline(admin.StackedInline):
	model = ParceiroExterno
	extra = 0 

class LinkInline(admin.StackedInline):
	model = Link
	extra = 0

class InstituicaoAdmin(admin.ModelAdmin):
	inlines = [ParceiroExternoInline, ParceiroInternoInline, LinkInline]
	fieldsets = [('informacoes de instituicao', {'fields': ['nome', 'telefone', 'celular', 'email']}), ('informacoes de responsavel', {'fields': ['nome_responsavel', 'email_responsavel', 'telefone_responsavel']}), ]


admin.site.register(Voluntario, VoluntarioAdmin)
admin.site.register(Instituicao, InstituicaoAdmin)
#admin.site.register(Curso)



# Register your models here.
