from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.listaDeOportunidades, name='listaDeOportunidades'),
    path('cadastroOportunidade', views.cadastroOportunidade, name = 'cadastroOportunidade'),
    path('cadastrarCurriculo', views.cadastrarCurriculo, name = 'cadastrarCurriculo'),
    path('dicas', views.dicas, name = 'dicas'),
    path('homeRecrutador', views.homeRecrutador, name = 'homeRecrutador'),
    path('oportunidade/<int:chavePrimaria>', views.oportunidade, name = 'Oportunidade'),
    path('curriculo/<int:chavePrimaria>', views.curriculo, name = 'Curriculo'),
    path('entrarOportunidade/<int:chavePrimaria>',views.entrarOportunidade, name = 'EntrarOportunidade'),
    path('quantidadeDeCurriculos/', views.numeroCurriculos, name = 'quantidadeDeCurriculos'),
    path('contato', views.contato, name = 'contato')
 ]
