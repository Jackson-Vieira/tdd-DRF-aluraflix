from django.test import TestCase
from ..models import Programa


class ProgramaModelTest(TestCase):
    def setUp(self) -> None:
        self.programa = Programa(
            titulo="Programa Teste",
            tipo="S",
            data_lancamento="2016-07-15",
        )

    def test_default_model_values(self):
        """Verifica os valores default do modelo"""
        self.assertEqual(self.programa.likes, 0)
        self.assertEqual(self.programa.dislikes, 0)

    def test_str(self):
        self.assertEqual(str(self.programa), "Programa Teste")
