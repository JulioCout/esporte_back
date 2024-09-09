from rest_framework import serializers
from academiadata.models import Aluno, Modalidade, Matricula

class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = '__all__'

class ModalidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Modalidade
        fields = '__all__'

class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        fields = '__all__'

class ListaMatriculasPorAlunoSerializer(serializers.ModelSerializer):
    modalidade = serializers.ReadOnlyField(source='modalidade.descricao')
    periodo = serializers.SerializerMethodField()
    class Meta:
        model = Matricula
        fields = ['modalidade', 'periodo']
    
    def get_periodo(self, obj):
        return obj.get_periodo_display()
    
class ListaMatriculasPorModalidadeSerializer(serializers.ModelSerializer):
    aluno_nome = serializers.ReadOnlyField(source='aluno.nome')
    class Meta:
        model = Matricula
        fields = ['aluno_nome']
