import requests
import allure
from url import URL

class OrderMethods:

    @staticmethod
    @allure.step("Создание заказа")
    def create_order(order_data: dict):
        return requests.post(URL.ORDER, json=order_data, verify = False)