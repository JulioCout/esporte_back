from django.contrib import admin
from django.urls import path, include
from academiadata.views import AlunoViewSet, ModalidadeViewSet, MatriculaViewSet, ListaMatriculasDoAluno, ListaMatriculasDaModalidade
from rest_framework import routers

router = routers.DefaultRouter()
router.register('alunos', AlunoViewSet, basename='Alunos')
router.register('modalidades', ModalidadeViewSet, basename='Modalidades')
router.register('matriculas', MatriculaViewSet, basename='Matricula')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('alunos/<int:pk>/matriculas', ListaMatriculasDoAluno.as_view()),
    path('modalidades/<int:pk>/matriculas', ListaMatriculasDaModalidade.as_view())
]
