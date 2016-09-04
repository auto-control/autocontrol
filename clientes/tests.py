from django.test import TestCase
from .models import clienteModel

class ClientesTest(TestCase):
	fixtures = ['clientes.json']

	def setUp(self):
		self.cliente = clienteModel()

	def test_numero_elementos(self):
		self.assertEqual(4, len(clienteModel.objects.all()))