import requests
import allure
from url import URL

class ListOrderMethods:

    @staticmethod
    @allure.step("Проверка списка заказов")
    def list_order():
        return requests.get(URL.ORDER, verify = False)