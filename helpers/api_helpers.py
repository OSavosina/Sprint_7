import random
import string
from client.services import post_v1, get_v1
from constants import RoutesName
from data import OrderData


def generate_fields_user(user_data):
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    fields_collection={}

    for field in user_data:
        fields_collection[field] = generate_random_string(10)

    return fields_collection



def create_user(data):
    return post_v1(RoutesName.COURIER, data)

def login_user(data):
    return post_v1(RoutesName.LOGIN_USER, data)

def create_order(color):
    prepare_data = OrderData.ORDER_FIELDS
    prepare_data["color"] = color
    return post_v1(RoutesName.ORDERS, prepare_data)

def get_orders_list(path):
    return get_v1(path)