from django.db import models
from django.core.urlresolvers import reverse
from django.urls import reverse #Used to generate URLs by reversing the URL patterns
import uuid # Required for unique book instances


# Create your models here.


class Curso(models.Model):
	#Modelo referente ao curso
	curso_nome = models.CharField(max_length=200)
	TIPO_CURSO = (
		('b', 'Bacharel'),
		('e', 'Educacao'),
		('s', 'Saude'),
		('l', 'Licenciatura'),
	)
	tipo = models.CharField(max_length=1, choices=TIPO_CURSO, blank=True, default='b')
	def __unicode__(self):
		return self.curso_nome

	def get_absolute_url(self):
		return reverse('curso_edit', kwargs={'pk': self.pk})

class Usuario(models.Model):
	"""
	Modelo do usuário
	"""
	nome = models.CharField(max_length=200)
	cargo = models.CharField(max_length=200)
	matricula = models.CharField(max_length=200)
	data_ingresso = models.DateField(null=True, blank=True)
	curso = models.ManyToManyField(Curso)
	def __unicode__(self):
		return self.nome

	def get_absolute_url(self):
		return reverse('usuario_edit', kwargs={'pk': self.pk})




class Acao(models.Model):
	#Modelo referente a Ação
	titulo = models.CharField(max_length=200)
	data_inicio = models.DateField(null=True, blank=True)
	data_fim = models.DateField(null=True, blank=True)
	TIPO_STATUS = (
		('e', 'Em andamento'),
		('c', 'Cancelado'),
		('f', 'Finalizado'),
		('a', 'Atrasado'),
	)
	status = models.CharField(max_length=1, choices=TIPO_STATUS, blank=True, default='b')
	def __unicode__(self):
		return self.titulo

	def get_absolute_url(self):
		return reverse('acao_edit', kwargs={'pk': self.pk})




class Avaliacao(models.Model):
	#Modelo referente a avaliação
	texto = models.CharField(max_length=250)
	data_semestre = models.DateField(null=True, blank=True)
	def __unicode__(self):
		return self.data_semestre

	def get_absolute_url(self):
		return reverse('avaliacao_edit', kwargs={'pk': self.pk})



class Questao(models.Model):
	#Modelo referente a questão
	TIPO_QUESTAO = (
		('b', 'Bacharel'),
		('e', 'Educacao'),
		('s', 'Saude'),
		('l', 'Licenciatura'),
	)
	tipo = models.CharField(max_length=1, choices=TIPO_QUESTAO, blank=True, default='b')
	enunciado1 = models.CharField(max_length=500)
	enunciado2 = models.CharField(max_length=500)
	enunciado3 = models.CharField(max_length=500)
	enunciado4 = models.CharField(max_length=500)
	enunciado5 = models.CharField(max_length=500)
	avaliacao = models.ForeignKey(Avaliacao)
	def __unicode__(self):
		return self.enunciado1

	def get_absolute_url(self):
		return reverse('questao_edit', kwargs={'pk': self.pk})



class Escolha_questao(models.Model):
	#Modelo referente a resposta que o usuario deu
	TIPO_ESCOLHA = (
		('1', 'Nulo'),
		('2', 'Ruim'),
		('3', 'Razoável'),
		('4', 'Bom'),
		('5', 'Muito bom'),
	)
	escolha = models.CharField(max_length=1, choices=TIPO_ESCOLHA, blank=True, default='3')
	questao = models.ForeignKey(Questao)
	def __unicode__(self):
		return self.escolha

	def get_absolute_url(self):
		return reverse('escolha_questao_edit', kwargs={'pk': self.pk})



class Resultado(models.Model):
	#agregador do curso com a avaliacao
	curso = models.ForeignKey(Curso)
	avaliacao = models.ForeignKey(Avaliacao)
	def __unicode__(self):
		return self.curso

	def get_absolute_url(self):
		return reverse('resultado_edit', kwargs={'pk': self.pk})



class Resposta(models.Model):
	#agregador das respostas dadas com as questoes
	resultado = models.ForeignKey(Resultado)
	questao = models.ForeignKey(Questao)
	escolha_questao = models.ForeignKey(Escolha_questao)
	def __unicode__(self):
		return self.resultado

	def get_absolute_url(self):
		return reverse('resposta_edit', kwargs={'pk': self.pk})
