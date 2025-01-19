import pytest
from helpers.api_helpers import generate_fields_user, create_user, login_user
from data import FixtureData


@pytest.fixture()
def fixture_generate_full_fields_for_user():
    return generate_fields_user(FixtureData.FULL_DICTIONARY_FIELDS)


@pytest.fixture
def fixture_create_user(fixture_generate_full_fields_for_user):
    return create_user(fixture_generate_full_fields_for_user)

@pytest.fixture
def fixture_create_user_with_lost_field():
    prepare_data = generate_fields_user(FixtureData.LOGIN_AND_FIRSTNAME_FIELDS)
    return create_user(prepare_data)

@pytest.fixture
def fixture_create_user_with_conflict(fixture_generate_full_fields_for_user):
    prepare_data = fixture_generate_full_fields_for_user
    create_user(prepare_data)
    return create_user(prepare_data)


@pytest.fixture
def fixture_login_user():
    prepare_data = generate_fields_user(FixtureData.FIELDS_FOR_LOGIN)
    create_user(prepare_data)
    return login_user(prepare_data)

@pytest.fixture
def fixture_login_user_error():
    prepare_data = generate_fields_user(FixtureData.NOT_FULL_FIELDS_FOR_LOGIN)
    create_user(prepare_data)
    return login_user(prepare_data)

@pytest.fixture
def fixture_login_user_not_found():
    prepare_data = generate_fields_user(FixtureData.FIELDS_FOR_LOGIN)
    return login_user(prepare_data)
