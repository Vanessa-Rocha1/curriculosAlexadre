from django.db import models
from django.conf import settings
# Create your models here.

class Curriculo(models.Model):
	nome = models.CharField(max_length = 150)
	generoChoises = (('Masculino', 'Masculino'), ('Feminino', 'Feminino'), ('Outro', 'Outro'))
	genero = models.CharField(choices = generoChoises, max_length = 10, default = 'O')
	dataNascimento = models.DateField()
	estadoCivilChoises = (('Solteiro','Solteiro'), ('Casado', 'Casado'), ('Divorsicado', 'Divorsicado'), ('Viuvo', 'Viuvo'), ('Separado', 'Separado'))
	estadoCivil = models.CharField(choices = estadoCivilChoises, max_length = 15, default = 'S')
	telefone =  models.CharField(max_length = 15)
	email =  models.CharField(max_length = 150)
	cep =  models.CharField(max_length = 10)
	logradouro =  models.CharField(max_length = 150)
	numero =  models.CharField(max_length = 15)
	bairro =  models.CharField(max_length = 150)
	cidade =  models.CharField(max_length = 150)
	ufChoises = (('AC', 'AC'), ('AL', 'AL'), ('AO', 'AO'), ('AM', 'AM'), ('BA', 'BA'), ('CE', 'CE'), ('DF', 'DF'), ('ES', 'ES'), ('GO', 'GO'), ('MA', 'MA'), ('MT', 'MT'), ('MS', 'MT'), ('MG', 'MG'), ('PA', 'PA'), ('PB', 'PB'), ('PR', 'PR'), ('PE', 'PE'), ('PI', 'PI'), ('RJ', 'RJ'), ('RN', 'RN'), ('RS', 'RS'), ('RO', 'RO'), ('RR', 'RR'), ('SC', 'SC'), ('SP',' SP'), ('SE', 'SE'), ('TP','TP'))
	uf = models.CharField(choices = ufChoises, max_length = 15, default = 'AC')
	pais =  models.CharField(max_length = 150)
	resumoProfissional =  models.TextField()
	objetivoProfissional =  models.TextField()
	nivelDeFormacao = models.TextField()
	instituicaoDeEnsino = models.CharField(max_length = 200)
	curso = models.CharField(max_length = 200)
	situacaoChoises = (('EM ANDAMENTO', 'EM ANDAMENTO'), ('CONCLUIDO', 'CONCLUIDO'))
	sitaucao = models.CharField(choices = situacaoChoises, max_length = 20, default = 'AN')
	anoDeConclusao = models.DateField()
	empresa  = models.CharField(max_length = 200)
	cargo = models.CharField(max_length = 150)
	dataInicial = models.DateField()
	dataFinal = models.DateField()
	atividades = models.TextField()
	dono = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)

class Oportunidade(models.Model):
	autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
	nome = models.CharField(max_length = 200)
	localChoises = (('CR', 'CURITIBA'), ('JN', 'JOINVILLE'), ('SP', 'SÃO PAULO'), ('OT', 'OUTRO'))
	local = models.CharField(choices = localChoises, max_length = 2, default = 'CR')
	descricao = models.TextField()
	atribuicao = models.TextField()
	interessados = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name = 'interessados')


