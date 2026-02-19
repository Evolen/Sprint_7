import pytest
import allure
from api_methods.list_order_methods import ListOrderMethods

class TestListOrder:

    @allure.title("Получение списказ аказов")
    @allure.description("Получение списка заказов")
    def test_list_order(self, list_order):
        response = list_order       
        assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
        assert response.json()["orders"]