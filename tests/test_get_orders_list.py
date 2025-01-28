from client.services import service_get_orders_list
from constants import RoutesName
import allure

# Для запросов со списком заказов response.json() возвращается с ошибками. Непонятно какой формат данных должен вернуться, в доке не описан.
class TestGetOrder:
    @allure.title('Получение списка заказов')
    def test_get_orders_list_success(self):
        response = service_get_orders_list(RoutesName.ALL_ORDERS)
        assert response.status_code == 200

    @allure.title('Ошибка получения списка заказов с несуществующим courierId')
    def test_get_orders_list_courier_id_not_found(self):
        response = service_get_orders_list(RoutesName.COURIER_NOT_FOUND_ID)
        assert response.status_code == 404

    @allure.title('Получение списка заказов рядом с метро Бульвар Рокоссовского')
    def test_get_order_near_station_success(self):
        response = service_get_orders_list(RoutesName.NEAREST_STATIONS_ORDERS)
        assert response.status_code == 200

    @allure.title('Получение списка из 10 заказов')
    def test_get_ten_orders_success(self):
        response = service_get_orders_list(RoutesName.TEN_ORDERS)
        assert response.status_code == 200

    @allure.title('Получение списка из 10 заказов, рядом с метро Калужская')
    def test_get_ten_orders_near_kaluzkaya_station_success(self):
        response = service_get_orders_list(RoutesName.TEN_ORDERS_NEAREST_STATION_KALUZKAYA)
        assert response.status_code == 200