import allure
from confest import fixture_create_user, fixture_create_user_with_lost_field, fixture_create_user_with_conflict
from constants import TestsMessages


class TestCreateUser:
    @allure.title('Успешное создание юзера')
    def test_create_user_success(self, fixture_create_user):
        response = fixture_create_user
        message = response.json()
        assert response.status_code == 201 and message['ok'] == True

    @allure.title('Создание юзера с неполным набором полей')
    def test_create_user_error(self, fixture_create_user_with_lost_field):
        response = fixture_create_user_with_lost_field
        message = response.json()
        assert response.status_code == 400 and message['message'] == TestsMessages.CREATE_USER_ERROR

    @allure.title('Создание двух одинаковых юзеров')
    def test_create_user_conflict(self, fixture_create_user_with_conflict):
        response = fixture_create_user_with_conflict
        message = response.json()
        assert response.status_code == 409 and message['message'] == TestsMessages.CREATE_USER_CONFLICT
