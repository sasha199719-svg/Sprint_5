import random

def generate_email():
    number = random.randint(1000, 9999)
    return f"testemail{number}@yandex.ru"

def generate_password():
    return "123456"

def generate_user():
    number = random.randint(1000, 9999)
    return f"TestUser{number}"