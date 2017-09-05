from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from questionario.models import Usuario, Curso, Acao, Questao

# Create your views here.

def index(request):
    """
    View function for home page of site.
    """
    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'index.html',
    )
#--------------------------- CRUD USUARIO ------------------------------
class UsuarioList(ListView):
	model = Usuario

class UsuarioCreate(CreateView):
	model = Usuario
	sucess_url = reverse_lazy('usuario_list')
	fields = ['nome', 'cargo', 'matricula', 'data_ingresso', 'curso']

class UsuarioUpdate(UpdateView):
	model = Usuario
	sucess_url = reverse_lazy('usuario_list')
	fields = ['nome', 'cargo', 'matricula', 'data_ingresso', 'curso']

class UsuarioDelete(DeleteView):
	model = Usuario
	sucess_url = reverse_lazy('usuario_list')
#--------------------------- CRUD USUARIO ------------------------------

#--------------------------- CRUD CURSO --------------------------------
class CursoList(ListView):
	model = Curso

class CursoCreate(CreateView):
	model = Curso
	sucess_url = reverse_lazy('curso_list')
	fields = ['curso_nome', 'tipo']

class CursoUpdate(UpdateView):
	model = Curso
	sucess_url = reverse_lazy('curso_list')
	fields = ['curso_nome', 'tipo']

class CursoDelete(DeleteView):
	model = Curso
	sucess_url = reverse_lazy('curso_list')
#--------------------------- CRUD CURSO --------------------------------

#--------------------------- CRUD AÇÃO ---------------------------------
class AcaoList(ListView):
	model = Acao

class AcaoCreate(CreateView):
	model = Acao
	sucess_url = reverse_lazy('acao_list')
	fields = ['titulo', 'data_inicio', 'data_fim', 'status']

class AcaoUpdate(UpdateView):
	model = Acao
	sucess_url = reverse_lazy('acao_list')
	fields = ['titulo', 'data_inicio', 'data_fim', 'status']

class AcaoDelete(DeleteView):
	model = Acao
	sucess_url = reverse_lazy('acao_list')
#--------------------------- CRUD AÇÃO ---------------------------------

#--------------------------- CRUD Questão ------------------------------

class QuestaoList(ListView):
	model = Questao

class QuestaoCreate(CreateView):
	model = Questao
	sucess_url = reverse_lazy('questao_list')
	fields = ['tipo', 'enunciado1', 'enunciado2', 'enunciado3', 'enunciado4', 'enunciado5', 'avaliacao']

class QuestaoUpdate(UpdateView):
	model = Questao
	sucess_url = reverse_lazy('questao_list')
	fields = ['tipo', 'enunciado1', 'enunciado2', 'enunciado3', 'enunciado4', 'enunciado5', 'avaliacao']

class QuestaoDelete(DeleteView):
	model = Questao
	sucess_url = reverse_lazy('questao_list')