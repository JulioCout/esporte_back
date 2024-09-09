from academiadata.models import Aluno, Modalidade, Matricula
from academiadata.serializers import AlunoSerializer, ModalidadeSerializer, MatriculaSerializer, ListaMatriculasPorAlunoSerializer, ListaMatriculasPorModalidadeSerializer
from rest_framework import viewsets, generics

class AlunoViewSet(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

class ModalidadeViewSet(viewsets.ModelViewSet):
    queryset = Modalidade.objects.all()
    serializer_class = ModalidadeSerializer

    
class MatriculaViewSet(viewsets.ModelViewSet):
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer

class ListaMatriculasDoAluno(generics.ListAPIView):
    def get_queryset(self):
        queryset = Matricula.objects.filter(aluno_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaMatriculasPorAlunoSerializer

class ListaMatriculasDaModalidade(generics.ListAPIView):
    def get_queryset(self):
        queryset = Matricula.objects.filter(modalidade_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaMatriculasPorModalidadeSerializer