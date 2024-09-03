from academiadata.models import Aluno, Modalidade
from academiadata.serializers import AlunoSerializer, ModalidadeSerializer
from rest_framework import viewsets

class AlunoViewSet(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

class ModalidadeViewSet(viewsets.ModelViewSet):
    queryset = Modalidade.objects.all()
    serializer_class = ModalidadeSerializer

    
