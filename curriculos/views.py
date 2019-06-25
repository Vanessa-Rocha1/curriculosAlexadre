from django.shortcuts import render, redirect
from .models import Oportunidade, Curriculo
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .forms import oportunidadeFormulario, curriculoFormulario, ContatoForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib import messages



def listaDeOportunidades(request):
	oportunidadesCadastradas = Oportunidade.objects.all()

	return render(request, 'html/lista-oportunidades-recrutador.html', {'oportunidades':oportunidadesCadastradas}) 

def dicas(request):
	return render(request, 'html/dicas-candidato.html', {}) 

def homeRecrutador(request):
	curriculos = Curriculo.objects.all()
	return render(request, 'html/home-recrutador.html', {'curriculos':curriculos})

def oportunidade(request, chavePrimaria):
	oportunidade = Oportunidade.objects.get(pk = chavePrimaria)
	interessados = oportunidade.interessados.all()
	return render(request, 'html/oportunidade.html', {'oportunidade':oportunidade, 'interessados': interessados}) 
	
def curriculo(request, chavePrimaria):
	curriculo = Curriculo.objects.get(pk = chavePrimaria)
	return render(request, 'html/curriculo.html', {'curriculo':curriculo})

def numeroCurriculos(request):
	curriculos = Curriculo.objects.count()
	return HttpResponse(curriculos, content_type="text/html")

@login_required
def cadastroOportunidade(request):
	oportunidade = oportunidadeFormulario()
	if request.method == "POST":
		oportunidade = oportunidadeFormulario(request.POST)
		if oportunidade.is_valid():
			oportunidade = oportunidade.save(commit = False)
			oportunidade.autor = request.user
			oportunidade.published_date = timezone.now()
			oportunidade.save()
			messages.success(request, 'Oportunidade criada com sucesso', extra_tags='alert')
			return redirect('listaDeOportunidades')

	return render(request, 'html/cadastrar-oportunidade.html', {'cadastro':oportunidade})

@login_required
def cadastrarCurriculo(request):
	curriculo = curriculoFormulario()
	if request.method == "POST":
		curriculo = curriculoFormulario(request.POST)
		print(curriculo.errors)
		if curriculo.is_valid():
			curriculo = curriculo.save(commit = False)
			curriculo.published_date = timezone.now()
			curriculo.dono = request.user
			curriculo.save()
			messages.success(request, 'Curriculo criado com sucesso', extra_tags='alert')
			return redirect('listaDeOportunidades')
	return render(request, 'html/candidato-curriculo.html', {'curriculo':curriculo})

@login_required
def entrarOportunidade(request, chavePrimaria):
	oportunidade = Oportunidade.objects.get(pk = chavePrimaria)
	oportunidade.interessados.add(request.user)
	return redirect('listaDeOportunidades')

def contato(request):
	if request.method == 'GET':
		email_form = ContatoForm()
	else:
		email_form = ContatoForm(request.POST)
		if email_form.is_valid():
			emissor = email_form.cleaned_data['emissor']
			assunto = email_form.cleaned_data['assunto']
			msg = email_form.cleaned_data['msg']


			send_mail(assunto, msg, emissor, [''])
			
			return redirect('listaDeOportunidades')
	return render(request, 'html/contato.html', {'form': email_form})




