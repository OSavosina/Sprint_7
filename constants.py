class HostName:
    HOST_NAME = 'http://qa-scooter.praktikum-services.ru/api/v1'
    HOST_NAME_FOR_ORDERS = 'http://qa-scooter.praktikum-services.ru/v1'

class RoutesName:
    COURIER = '/courier'
    LOGIN_USER = '/courier/login'
    ORDERS = '/orders'
    ALL_ORDERS = '/orders?courierId=1'
    COURIER_NOT_FOUND_ID = '/orders?courierId=0001'
    NEAREST_STATIONS_ORDERS = '/orders?courierId=1&nearestStation=["1"]'
    TEN_ORDERS = '/orders?limit=10&page=0'
    TEN_ORDERS_NEAREST_STATION_KALUZKAYA = '/orders?limit=10&page=0&nearestStation=["110"]'




