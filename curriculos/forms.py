from django import forms

from .models import Oportunidade, Curriculo

class oportunidadeFormulario(forms.ModelForm):
	class Meta:
		model = Oportunidade
		fields = ('nome', 'local', 'descricao', 'atribuicao')

class curriculoFormulario(forms.ModelForm):
	
	class Meta:
		model = Curriculo
		fields = ('nome', 'genero', 'dataNascimento', 'estadoCivil', 'telefone', 'email', 'cep', 'logradouro', 'numero', 'numero', 'bairro', 'cidade', 'uf', 'pais', 'pais', 'resumoProfissional', 'objetivoProfissional', 'nivelDeFormacao', 'instituicaoDeEnsino', 'curso', 'sitaucao', 'anoDeConclusao', 'empresa', 'cargo', 'dataInicial', 'dataFinal', 'atividades')


class ContatoForm(forms.Form):
	emissor = forms.EmailField(required=True, label='Remetente')
	assunto = forms.CharField(required=True)
	msg = forms.CharField(widget=forms.Textarea, label='Mensagem')