from conftest import fixture_generate_full_fields_for_user, fixture_create_user_with_lost_field, fixture_create_user_with_conflict
import allure

class TestCreateUser:
    @allure.title('Успешное создание юзера')
    def test_create_user_success(self, fixture_generate_full_fields_for_user):
        response = fixture_generate_full_fields_for_user
        assert response.status_code == 201

    @allure.title('Создание юзера с неполным набором полей')
    def test_create_user_error(self, fixture_create_user_with_lost_field):
        response = fixture_create_user_with_lost_field
        assert response.status_code == 400

    @allure.title('Создание двух одинаковых юзеров')
    def test_create_user_conflict(self, fixture_create_user_with_conflict):
        response = fixture_create_user_with_conflict
        assert response.status_code == 409
