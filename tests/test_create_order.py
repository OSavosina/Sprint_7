import pytest
from client.services import service_create_order
import allure


class TestCreateOrder:
    @allure.title('Успешное создание заказа')
    @pytest.mark.parametrize('color', [['BLACK'], ['BLACK', 'GREY'], []])
    def test_create_order_success(self, color):
        response = service_create_order(color)
        message = response.json()
        assert response.status_code == 201 and message["track"] == 124124
