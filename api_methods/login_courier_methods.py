import requests
import allure
from url import URL


class LoginCourierMethods:

    @staticmethod
    @allure.step("Логин курьера")
    def login_courier(courier_data: dict):
        return requests.post(URL.LOGIN_COURIER, json = courier_data, verify = False)

    @staticmethod
    @allure.step("Проверка ввода на неправильный логин")
    def fake_login_courier(courier_data: dict):
        return requests.post(URL.LOGIN_COURIER, json = courier_data, verify = False)

    @staticmethod
    @allure.step("Проверка ввода на неправильный пароль")
    def fake_pass_courier(courier_data: dict):
        return requests.post(URL.LOGIN_COURIER, json = courier_data, verify = False)  

    @staticmethod
    @allure.step("Проверка ввода без логина")
    def not_login_courier(courier_data: dict):
        return requests.post(URL.LOGIN_COURIER, json = courier_data, verify = False)      

    @staticmethod
    @allure.step("Проверка ввода без пароля")
    def not_pass(courier_data: dict):
        return requests.post(URL.LOGIN_COURIER, json = courier_data, verify = False)     

    @staticmethod
    @allure.step("Проверка ошибки при вводе не верных данных")
    def fake_pass_login(courier_data: dict):
        return requests.post(URL.LOGIN_COURIER, json = courier_data, verify = False)     

        