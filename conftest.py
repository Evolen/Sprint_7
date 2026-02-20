import pytest
from api_methods.order_methods import OrderMethods

from generators import generate_random_courier_dict
from api_methods.create_courier_methods import CreateCourierMethods
from api_methods.login_courier_methods import LoginCourierMethods
from api_methods.list_order_methods import ListOrderMethods
from data import *


    
@pytest.fixture
def create_random_courier(scope="function"):
    courier_body = generate_random_courier_dict()    
    return courier_body

@pytest.fixture
def create_courier_without_login(scope="function"):
    courier_body = CREATER_COURIER_WITHOUT_LOGIN 
    response = CreateCourierMethods.create_courier(courier_data = courier_body)
    return response   

@pytest.fixture
def create_courier_login_again(scope="function"):
    courier_body = CREATER_COURIER_LOGIN_AGAIN 
    response = CreateCourierMethods.create_courier(courier_data = courier_body)
    return response  

@pytest.fixture
def courier_login(scope="function"):
    courier_body = COURIER_LOGIN 
    response = LoginCourierMethods.login_courier(courier_data = courier_body)
    return response  

@pytest.fixture
def courier_pass(scope="function"):
    courier_body = FAKE_PASS
    response = LoginCourierMethods.fake_pass_courier(courier_data = courier_body)
    return response   

@pytest.fixture
def no_login(scope="function"):
    courier_body = WITHOUT_LOGIN
    response = LoginCourierMethods.not_login_courier(courier_data = courier_body)
    return response  

@pytest.fixture
def not_pass(scope="function"):
    courier_body = WITHOUT_PASS
    response = LoginCourierMethods.not_pass(courier_data = courier_body)
    return response 

@pytest.fixture
def fake_pass_login(scope="function"):
    courier_body = FAKE_PASS_LOGIN
    response = LoginCourierMethods.fake_pass_login(courier_data = courier_body)
    return response    

@pytest.fixture
def list_order(scope="function"):
    response = ListOrderMethods.list_order()
    return response    