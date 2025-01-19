import requests
from constants import HostName


def post_v1(path='', data=None):
    return requests.post(f'{HostName.HOST_NAME}{path}', data)

def get_v1(path=''):
    return requests.get(f'{HostName.HOST_NAME_FOR_ORDERS}{path}')