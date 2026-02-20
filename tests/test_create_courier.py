import pytest
import allure

from api_methods.create_courier_methods import CreateCourierMethods


class TestCreateCourier:

    @allure.title("Создание курьера")
    @allure.description("Проверка создания курьера")
    def test_create_courier(self, create_random_courier):    
        response = CreateCourierMethods.create_courier(courier_data = create_random_courier)
        assert response.status_code == 201, f"Expected status code 201, but got {response.status_code}"
        assert response.json()["ok"] == True          
        

    @allure.description("Проверка создания курьера, который уже был создан")
    def test_create_courier_again(self, create_random_courier):
        response = CreateCourierMethods.create_courier(courier_data = create_random_courier)
        response = CreateCourierMethods.create_courier(courier_data = create_random_courier)
        assert response.status_code == 409, f"Expected status code 409, but got {response.status_code}"
        assert response.json()["message"] == "Этот логин уже используется. Попробуйте другой."

    @allure.description("Проверка создания курьера без имени")
    def test_create_courier_without_login (self, create_courier_without_login):
        response = CreateCourierMethods.create_courier(courier_data = create_courier_without_login)   
        assert response.status_code == 400, f"Expected status code 400, but got {response.status_code}"
        assert response.json()["message"] == "Недостаточно данных для создания учетной записи"

    @allure.description("Проверка создания курьера с существующим логином")
    def test_create_courier_login_again (self, create_courier_login_again):
        response = create_courier_login_again    
        assert response.status_code == 409, f"Expected status code 409, but got {response.status_code}"
        assert response.json()["message"] == "Этот логин уже используется"
