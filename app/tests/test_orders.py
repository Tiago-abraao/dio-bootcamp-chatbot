import unittest
from unittest.mock import patch

from orders import consultar_pedido


class TestConsultarPedido(unittest.TestCase):
    def test_consulta_pedido_existente(self):
        resultado = consultar_pedido(1001)

        self.assertIn("Encontrei o seu pedido 1001!", resultado)

    def test_consulta_pedido_inexistente(self):
        resultado2 = consultar_pedido(9999)

        self.assertEqual("Pedido não encontrado.", resultado2)

    @patch("orders.buscar_pedido")
    def test_consulta_com_mock(self, mock_buscar):
        mock_buscar.return_value = (1002, "Headset sem fio", "Entregue")

        resultado = consultar_pedido(1002)

        self.assertIn("Headset sem fio", resultado)
        mock_buscar.assert_called_once_with(1002)