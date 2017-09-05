from django.contrib import admin
from .models import Curso, Usuario, Acao, Avaliacao, Questao

admin.site.register(Curso)
admin.site.register(Usuario)
admin.site.register(Acao)
admin.site.register(Avaliacao)
admin.site.register(Questao)
