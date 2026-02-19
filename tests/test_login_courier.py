import pytest
import allure

from api_methods.login_courier_methods import LoginCourierMethods

class TestLoginCourier:

    @allure.title("Проверка логина")
    @allure.description("Проверка существующего логина")
    def test_login_courier(self, courier_login):
        response = courier_login    
        assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
        assert response.json()["id"] == 704064

    
    @allure.description("Проверка на ошибку, если неправильно указать логин")
    def test_fake_login_courier(self, courier_login):
        response = courier_login    
        assert response.status_code == 404, f"Expected status code 404 but got {response.status_code}"
        assert response.json()["message"] == "Учетная запись не найдена"

    @allure.description("Проверка на ошибку, если неправильно указать пароль")
    def test_fake_pass_courier(self, courier_pass):
        response = courier_pass   
        assert response.status_code == 404, f"Expected status code 404 but got {response.status_code}"
        assert response.json()["message"] == "Учетная запись не найдена"

    @allure.description("Проверка на ошибку, если нет поля логина")
    def test_no_login(self, no_login):
        response = no_login  
        assert response.status_code == 400, f"Expected status code 400 but got {response.status_code}"
        assert response.json()["message"] == "Недостаточно данных для входа"   

    @allure.description("Проверка на ошибку, если нет поля пароля")
    @allure.description("Проверка на ошибку, если нет поля пароля")
    def test_no_pass(self, not_pass):
        response = not_pass   
        assert response.status_code == 400, f"Expected status code 400 but got {response.status_code}"
        assert response.json()["message"] == "Недостаточно данных для входа"    

    @allure.description("Проверка на ошибку с ошибочными данными")
    def test_no_pass_login(self, fake_pass_login):
        response = fake_pass_login  
        assert response.status_code == 404, f"Expected status code 404 but got {response.status_code}"
        assert response.json()["message"] == "Учетная запись не найдена"       