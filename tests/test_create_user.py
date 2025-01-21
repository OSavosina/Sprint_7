import allure
from helpers.helpers import create_user_with_lost_field, create_user_with_conflicts, \
    create_user


class TestCreateUser:
    @allure.title('Успешное создание юзера')
    def test_create_user_success(self):
        response = create_user()
        message = response.json()
        assert response.status_code == 201 and message['ok'] == True

    @allure.title('Создание юзера с неполным набором полей')
    def test_create_user_error(self):
        response = create_user_with_lost_field()
        message = response.json()
        assert response.status_code == 400 and message['message'] == 'Недостаточно данных для создания учетной записи'

    @allure.title('Создание двух одинаковых юзеров')
    def test_create_user_conflict(self):
        response = create_user_with_conflicts()
        message = response.json()
        assert response.status_code == 409 and message['message'] == 'Этот логин уже используется. Попробуйте другой.'
