import pytest
from helpers.api_helpers import create_order
import allure


class TestCreateOrder:
    @allure.title('Успешное создание заказа')
    @pytest.mark.parametrize('color', [['BLACK'], ['BLACK', 'GREY'], []])
    def test_create_order_success(self, color):
        response = create_order(color)
        assert response.status_code == 201 and response.json()["track"]
