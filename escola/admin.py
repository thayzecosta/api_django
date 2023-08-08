from django.contrib import admin
from escola.models import Aluno, Curso, Matricula


class Alunos(admin.ModelAdmin):
    list_display = ('id', 'nome', 'rg', 'cpf', 'data_nascimento')  # campos que queremos exibir no display do admin
    list_display_links = ('id', 'nome')  # para que, quando quisermos alterar algum aluno, =seja possível clicarmos no ID ou no nome do aluno.
    search_fields = ('nome',)  #  campo de busca onde possamos buscar os alunos pelo nome. Portanto, search_fields = ('nome',).
    list_per_page = 20  # paginação na quantidade de alunos. Assim, supondo que a nossa base de dados tenha 500 alunos, eles não serão exibidos de uma só vez. Definiremos, então, em 20 por página: list_per_page = 20.


admin.site.register(Aluno, Alunos)


class Cursos(admin.ModelAdmin):
    list_display = ('id', 'codigo_curso', 'descricao')
    list_display_links = ('id', 'codigo_curso')
    search_fields = ('codigo_curso',)

admin.site.register(Curso, Cursos)


class Matriculas(admin.ModelAdmin):
        list_display = ('id', 'aluno', 'curso', 'periodo')
        list_display_links = ('id',)

admin.site.register(Matricula, Matriculas)


