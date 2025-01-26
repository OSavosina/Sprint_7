import allure
from confest import fixture_login_user, fixture_login_user_error, fixture_login_user_not_found
from constants import TestsMessages

class TestLoginUser:
    @allure.title('Успешная авторизация юзера')
    def test_login_user_success(self, fixture_login_user):
        response = fixture_login_user
        message = response.json()
        assert response.status_code == 200 and message['id']

    @allure.title('Авторизация с неполным набором полей')
    def test_login_user_error(self, fixture_login_user_error):
        response = fixture_login_user_error
        message = response.json()
        assert response.status_code == 400 and message['message'] == TestsMessages.LOGIN_USER_ERROR

    @allure.title('Авторизация под несуществующим юзером')
    def test_login_user_not_found(self, fixture_login_user_not_found):
        response = fixture_login_user_not_found
        message = response.json()
        assert response.status_code == 404 and message['message'] == TestsMessages.LOGIN_USER_NOT_FOUND



