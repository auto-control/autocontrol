from django.test import TestCase
from .models import *

class vehiculoModelTest(TestCase):
	fixtures = ['vehiculos.json']

	def setUp(self):
		self.vehiculo = vehiculoModel()

	def test_numero_elementos(self):
		self.assertEqual(7, len(vehiculoModel.objects.all()))