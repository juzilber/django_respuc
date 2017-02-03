from __future__ import unicode_literals

from django.db import models

GENDER_CHOICES = (('Masculino', 'Masculino'), ('Feminino', 'Feminino'), ('Outros', 'Outros'), )

class Voluntario(models.Model):
	nome = models.CharField(max_length=50, null=False, blank=False)
	CPF = models.CharField(max_length=14, null=False, blank=False, unique=True, primary_key=True)
	matricula = models.CharField(max_length=7, null=False, blank=False, unique=True)
	genero = models.CharField(max_length=20, choices=GENDER_CHOICES, null=False, blank=False)
	periodo = models.IntegerField(null=False, blank=False)
	data_de_nascimento = models.DateField(null=False, blank=False)
	idioma = models.CharField(max_length=20)
	nome_do_curso = models.CharField(max_length=40, null=False, blank=False)
	rua = models.CharField(max_length=60, null=False, blank=False)
	numero = models.CharField(max_length=20, null=False, blank=False)
	complemento = models.CharField(max_length=15)
	bairro = models.CharField(max_length=20, null=False, blank=False)
	cidade = models.CharField(max_length=20, null=False, blank=False)
	estado = models.CharField(max_length=2, null=False, blank=False)
	CEP = models.CharField(max_length=9, null=False, blank=False)
	telefone_fixo = models.CharField(max_length=14, null=False, blank=False)
	celular = models.CharField(max_length=14, null=False, blank=False)
	email = models.CharField(max_length=60, null=False, blank=False, unique=True)

	def __str__(instance):
		return instance.matricula + ' - ' + instance.nome

class Instituicao(models.Model):
	nome = models.CharField(max_length=50, null=False, blank=False, primary_key=True)
	telefone = models.CharField(max_length=14, null=False, blank=False)
	celular = models.CharField(max_length=14, null=False, blank=False)
	email = models.CharField(max_length=60, null=False, blank=False, unique=True)
	vinculo = models.CharField(max_length=20, null=False, blank=False)
	nome_responsavel = models.CharField(max_length=50, null=False, blank=False)
	email_responsavel = models.CharField(max_length=100, null=False, blank=False)
	telefone_responsavel = models.CharField(max_length=20, null=False, blank=False)

class Link(models.Model):
	site = models.CharField(max_length=200, null=False, blank=False)
	instituicao = models.ForeignKey(Instituicao, on_delete=models.CASCADE, null=False, blank=False)

class ParceiroInterno(models.Model):
	ramal = models.CharField(max_length=10, null=False, blank=False)
	instituicao = models.OneToOneField(Instituicao, on_delete=models.CASCADE, null=False)


class ParceiroExterno(models.Model):
	CPF = models.CharField(max_length=14, null=False, blank=False)
	CNPJ = models.CharField(max_length=20, null=False, blank=False)
	endereco= models.CharField(max_length=60, null=False, blank=False)
	numero = models.CharField(max_length=20, null=False, blank=False)
	complemento = models.CharField(max_length=15)
	bairro = models.CharField(max_length=20, null=False, blank=False)
	cidade = models.CharField(max_length=20, null=False, blank=False)
	estado = models.CharField(max_length=2, null=False, blank=False)
	CEP = models.CharField(max_length=9, null=False, blank=False)
	instituicao = models.OneToOneField(Instituicao, on_delete=models.CASCADE, null=False)

class Curso(models.Model):
	nome = models.CharField(max_length=50, null=False, blank=False, primary_key=True)
	coordenador_do_curso = models.CharField(max_length=50, null=False, blank=False)
	departamento = models.CharField(max_length=20, null=False, blank=False)
	quantidade_de_alunos = models.IntegerField()
# Create your models here.



