import pytest
from helpers.helpers import generate_fields_user
from client.services import service_create_user, service_login_user
from data import TestsUserData


@pytest.fixture
def fixture_create_user():
    fields_collection = generate_fields_user(TestsUserData.FULL_DICTIONARY_FIELDS)
    return service_create_user(fields_collection)

@pytest.fixture
def fixture_create_user_with_lost_field():
    prepare_data = generate_fields_user(TestsUserData.LOGIN_AND_FIRSTNAME_FIELDS)
    return service_create_user(prepare_data)

@pytest.fixture
def fixture_create_user_with_conflict():
    prepare_data = generate_fields_user(TestsUserData.FULL_DICTIONARY_FIELDS)
    service_create_user(prepare_data)
    return service_create_user(prepare_data)


@pytest.fixture
def fixture_login_user():
    prepare_data = generate_fields_user(TestsUserData.FIELDS_FOR_LOGIN)
    service_create_user(prepare_data)
    return service_login_user(prepare_data)

@pytest.fixture
def fixture_login_user_error():
    prepare_data = generate_fields_user(TestsUserData.FIELDS_FOR_LOGIN)
    service_create_user(prepare_data)
    return service_login_user({'login': prepare_data['login']})

@pytest.fixture
def fixture_login_user_not_found():
    prepare_data = generate_fields_user(TestsUserData.FIELDS_FOR_LOGIN)
    return service_login_user(prepare_data)