from django.test import TestCase
from ..models import Programa
from ..serializers import ProgramaSerializer


class ProgramaSerializerTest(TestCase):
    def setUp(self):
        self.programa = Programa(
            titulo="Programa Teste",
            tipo="S",
            data_lancamento="2016-07-15",
            likes=2340,
            dislikes=40,
        )
        self.serializer = ProgramaSerializer(instance=self.programa)

    def test_serializer_fields(self):
        "Testar  fields que estao sendo utilizados no serializers"

        data = self.serializer.data
        result = set(["id", "titulo", "tipo",
                     "data_lancamento", "likes", "dislikes"])
        self.assertEqual(result, set(data.keys()))
