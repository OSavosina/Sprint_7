from client.api import post_v1, get_v1
from constants import RoutesName
from data import TestsOrderData
import allure


@allure.step('Создание юзера')
def service_create_user(data):
    return post_v1(RoutesName.COURIER, data)

@allure.step('Авторизация юзера')
def service_login_user(data):
    return post_v1(RoutesName.LOGIN_USER, data)

@allure.step('Создание заказа')
def service_create_order(color):
    prepare_data = TestsOrderData.ORDER_FIELDS
    prepare_data["color"] = color
    return post_v1(RoutesName.ORDERS, prepare_data)

@allure.step('Получение списка заказов')
def service_get_orders_list(path):
    return get_v1(path)