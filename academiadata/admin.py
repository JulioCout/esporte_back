from django.contrib import admin
from academiadata.models import Aluno, Modalidade, Matricula

# criar modelo
class Alunos(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email', 'cpf', 'data_nascimento', 'celular',)
    list_filter = ('id' ,'nome',)
    list_per_page = 20
    search_fields = ('nome',)

# registrar modelo
admin.site.register(Aluno, Alunos)


class Modalidades(admin.ModelAdmin):
    list_display = ('id', 'codigo', 'descricao',)
    list_display_links = ('id' ,'codigo',)
    search_fields = ('codigo',)

admin.site.register(Modalidade, Modalidades)

class Matriculas(admin.ModelAdmin):
    list_display = ('id', 'aluno', 'modalidade', 'periodo',)
    list_display_links = ('id',)

admin.site.register(Matricula, Matriculas)
