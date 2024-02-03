from django.test import TestCase
from vehiculos.models import Vehiculo

# Create your tests here.
class LaboratorioTests(TestCase):
    @classmethod
    def setUpTestData(cls):
      cls.x = Vehiculo()
      cls.x.precio = 1
      cls.x.save()

    def test_laboratorio_content(self):
      print("aaddd")
      
      print(">>", self.x)