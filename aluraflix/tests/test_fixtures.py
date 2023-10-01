from django.test import TestCase
from ..models import Programa


class FixtureDataTest(TestCase):
    fixtures = ["programas_iniciais"]

    def test_load_fixtures(self):
        programa_bizarro = Programa.objects.get(pk=1)
        count_programas = Programa.objects.count()
        self.assertEqual(programa_bizarro.titulo, 'Coisas bizarras')
        self.assertEqual(count_programas, 9)
