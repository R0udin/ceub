from django.conf.urls import url

from . import views


urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^usuarios$', views.UsuarioList.as_view(), name='usuario_list'),
	url(r'^novo_usuario$', views.UsuarioCreate.as_view(), name='usuario_new'),
	url(r'^editar_usuario/(?P<pk>\d+)$', views.UsuarioUpdate.as_view(), name='usuario_edit'),
	url(r'^deletar_usuario/(?P<pk>\d+)$', views.UsuarioDelete.as_view(), name='usuario_delete'),
	url(r'^cursos$', views.CursoList.as_view(), name='curso_list'),
	url(r'^novo_curso$', views.CursoCreate.as_view(), name='curso_new'),
	url(r'^editar_curso/(?P<pk>\d+)$', views.CursoUpdate.as_view(), name='curso_edit'),
	url(r'^deletar_curso/(?P<pk>\d+)$', views.CursoDelete.as_view(), name='curso_delete'),
	url(r'^acoes$', views.AcaoList.as_view(), name='acao_list'),
	url(r'^novo_acao$', views.AcaoCreate.as_view(), name='acao_new'),
	url(r'^editar_acao/(?P<pk>\d+)$', views.AcaoUpdate.as_view(), name='acao_edit'),
	url(r'^deletar_acao/(?P<pk>\d+)$', views.AcaoDelete.as_view(), name='acao_delete'),
	url(r'^questoes$', views.QuestaoList.as_view(), name='questao_list'),
	url(r'^nova_questao$', views.QuestaoCreate.as_view(), name='questao_new'),
	url(r'^editar_questao/(?P<pk>\d+)$', views.QuestaoUpdate.as_view(), name='questao_edit'),
	url(r'^deletar_questao/(?P<pk>\d+)$', views.QuestaoDelete.as_view(), name='questao_delete'),
]