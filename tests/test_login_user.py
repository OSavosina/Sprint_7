from conftest import fixture_login_user, fixture_login_user_error, fixture_login_user_not_found
import allure

class TestLoginUser:
    @allure.title('Успешная авторизация юзера')
    def test_login_user_success(self, fixture_login_user):
        response = fixture_login_user
        assert response.status_code == 200

    @allure.title('Авторизация с неполным набором полей')
    def test_login_user_error(self, fixture_login_user_error):
        response = fixture_login_user_error
        assert response.status_code == 400

    @allure.title('Авторизация под несуществующим юзером')
    def test_login_user_not_found(self, fixture_login_user_not_found):
        response = fixture_login_user_not_found
        assert response.status_code == 404



