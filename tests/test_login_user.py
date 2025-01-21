import allure
from helpers.helpers import login_user, login_user_error, login_user_not_found

class TestLoginUser:
    @allure.title('Успешная авторизация юзера')
    def test_login_user_success(self):
        response = login_user()
        message = response.json()
        assert response.status_code == 200 and message['id']

    @allure.title('Авторизация с неполным набором полей')
    def test_login_user_error(self):
        response = login_user_error()
        message = response.json()
        assert response.status_code == 400 and message['message'] == 'Недостаточно данных для входа'

    @allure.title('Авторизация под несуществующим юзером')
    def test_login_user_not_found(self):
        response = login_user_not_found()
        message = response.json()
        assert response.status_code == 404 and message['message'] == 'Учетная запись не найдена'



