import pytest
import allure

from api_methods.order_methods import OrderMethods
from generators import *

class TestCreateOrder:

    @allure.title("Создание заказа")
    @allure.description("Проверка создания заказа")
    @pytest.mark.parametrize("orderData, statusCode", [
        (generate_random_order_black_dict(), 201),
        (generate_random_order_grey_dict(), 201),
        (generate_random_order_black_grey_dict(), 201),
        (generate_random_order_no_color_dict(), 201)

    ])
    def test_create_order(self, orderData, statusCode):
        with allure.step("Отправляем запрос на создание заказа"):
            response = OrderMethods.create_order(order_data=orderData)
        assert response.status_code == statusCode, f"Expected status code {statusCode}, but got {response.status_code}"
        assert type(response.json()["track"]) == int

   






































    
       

