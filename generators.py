from faker import Faker
fake = Faker()


def generate_random_order_black_dict():
    return {
        "firstname": fake.first_name(),
        "lastname": fake.last_name(),
        "address": 	fake.address(),
        "metroStation": fake.random_int(min=1, max=6),
        "phone": fake.phone_number(),
        "rentTime": fake.random_int(min=1, max=7),
        "deliveryDate": fake.date(),
        "comment": fake.sentence(),
        "color": [
            "BLACK"
    ]
        
    }

def generate_random_order_grey_dict():
    return {
        "firstname": fake.first_name(),
        "lastname": fake.last_name(),
        "address": 	fake.address(),
        "metroStation": fake.random_int(min=1, max=6),
        "phone": fake.phone_number(),
        "rentTime": fake.random_int(min=1, max=7),
        "deliveryDate": fake.date(),
        "comment": fake.sentence(),
        "color": [
            "GREY"
            
    ]
        
    }

def generate_random_order_black_grey_dict():
    return {
        "firstname": fake.first_name(),
        "lastname": fake.last_name(),
        "address": 	fake.address(),
        "metroStation": fake.random_int(min=1, max=6),
        "phone": fake.phone_number(),
        "rentTime": fake.random_int(min=1, max=7),
        "deliveryDate": fake.date(),
        "comment": fake.sentence(),
        "color": [
            "BLACK"
            "GREY"
    ]
        
    }

def generate_random_order_no_color_dict():
    return {
        "firstname": fake.first_name(),
        "lastname": fake.last_name(),
        "address": 	fake.address(),
        "metroStation": fake.random_int(min=1, max=6),
        "phone": fake.phone_number(),
        "rentTime": fake.random_int(min=1, max=7),
        "deliveryDate": fake.date(),
        "comment": fake.sentence(),
        "color": [            
            
    ]
        
    }

def generate_random_courier_dict():
    return {
        "login": fake.user_name(),
        "password": fake.password(),
        "firstName": fake.first_name()
     
    }
    
    