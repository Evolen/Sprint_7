import requests
import allure
from url import URL


class CreateCourierMethods:

    @staticmethod
    @allure.step("Создание курьера")
    def create_courier(courier_data: dict):
        return requests.post(URL.CREATE_COURIER, json = courier_data, verify = False)

      
        
