from rest_framework import serializers
from aluraflix.models import Programa


class ProgramaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Programa
        fields = ["id", 'titulo', 'tipo',
                  'data_lancamento', 'likes', "dislikes"]
