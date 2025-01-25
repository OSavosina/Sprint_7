import pytest
from helpers.helpers import generate_fields_user, create_user, login_user
from data import TestsUserData


@pytest.fixture
def fixture_create_user():
    generate_fields_user(TestsUserData.FULL_DICTIONARY_FIELDS)
    create_user()

@pytest.fixture
def fixture_create_user_with_lost_field():
    prepare_data = generate_fields_user(TestsUserData.LOGIN_AND_FIRSTNAME_FIELDS)
    create_user(prepare_data)

@pytest.fixture
def fixture_create_user_with_conflict():
    prepare_data = generate_fields_user(TestsUserData.FULL_DICTIONARY_FIELDS)
    create_user(prepare_data)
    create_user(prepare_data)


@pytest.fixture
def fixture_login_user():
    prepare_data = generate_fields_user(TestsUserData.FIELDS_FOR_LOGIN)
    create_user(prepare_data)
    login_user(prepare_data)

@pytest.fixture
def fixture_login_user_error():
    prepare_data = generate_fields_user(TestsUserData.NOT_FULL_FIELDS_FOR_LOGIN)
    create_user(prepare_data)
    login_user(prepare_data)

@pytest.fixture
def fixture_login_user_not_found():
    prepare_data = generate_fields_user(TestsUserData.FIELDS_FOR_LOGIN)
    login_user(prepare_data)