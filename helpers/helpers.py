import random
import string
from data import TestsUserData
from client.services import service_create_user, service_login_user



def generate_fields_user(user_data):
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    fields_collection={}

    for field in user_data:
        fields_collection[field] = generate_random_string(10)

    return fields_collection

def generate_full_fields_for_user():
    return generate_fields_user(TestsUserData.FULL_DICTIONARY_FIELDS)


def create_user():
    fields_collection = generate_fields_user(TestsUserData.FULL_DICTIONARY_FIELDS)
    return service_create_user(fields_collection)

def create_user_with_lost_field():
    prepare_data = generate_fields_user(TestsUserData.LOGIN_AND_FIRSTNAME_FIELDS)
    return service_create_user(prepare_data)

def create_user_with_conflicts():
    prepare_data = generate_full_fields_for_user()
    service_create_user(prepare_data)
    return service_create_user(prepare_data)


def login_user():
    prepare_data = generate_fields_user(TestsUserData.FIELDS_FOR_LOGIN)
    service_create_user(prepare_data)
    return service_login_user(prepare_data)

def login_user_error():
    prepare_data = generate_fields_user(TestsUserData.NOT_FULL_FIELDS_FOR_LOGIN)
    service_create_user(prepare_data)
    return service_login_user(prepare_data)

def login_user_not_found():
    prepare_data = generate_fields_user(TestsUserData.FIELDS_FOR_LOGIN)
    return service_login_user(prepare_data)
