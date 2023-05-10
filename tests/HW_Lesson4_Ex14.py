import pytest #чтобы использовать parametrize
import requests

from lib.base_case import BaseCase
from lib.assertions import Assertions

class TesttUserRegister(BaseCase):
    datas  = [
        [('username'), ('learnqa'), ('firstName'), ('learnqa'), ('lastName'), ('learnqa'), ('email'), ('ne11y@example.com'), ('password')],
        [('password'), ('123'), ('firstName'), ('learnqa'), ('lastName'), ('learnqa'), ('email'), ('ne11y@example.com'),('username')],
        [('password'), ('123'), ('username'), ('learnqa'), ('lastName'), ('learnqa'), ('email'), ('ne11y@example.com'),('firstName')],
        [('password'), ('123'), ('username'), ('learnqa'), ('firstName'),  ('learnqa'), ('email'), ('ne11y@example.com'), ('lastName')],
        [('password'), ('123'), ('username'), ('learnqa'), ('firstName'), ('learnqa'), ('lastName'), ('learnqa'),('email')]
    ]




    def test_create_user_with_existing_email(self):
        email = 'vinkotov@example.com'
        data = {
            'password': '123',
            'username': 'learnqa',
            'firstName': 'learnqa',
            'lastName': 'learnqa',
            'email': email
        }

        response = requests.post("https://playground.learnqa.ru/api/user/", data=data)

        assert response.status_code == 400, f"Unexpected status code '{response.status_code}"
        assert response.content.decode("utf-8") == f"Users with email '{email}' already exists", f"Unexpected response content '{response.content}"

    def test_create_user_with_incorrect_email(self):
        email = 'vinkotov.example.com'
        data = {
            'password': '123',
            'username': 'learnqa',
            'firstName': 'learnqa',
            'lastName': 'learnqa',
            'email': email
        }

        response2 = requests.post("https://playground.learnqa.ru/api/user/", data=data)

        #print(response2.status_code)
        #print(response2.content)

        assert response2.status_code == 400, f"Unexpected status code '{response2.status_code}"
        assert response2.content.decode("utf-8") == f"Invalid email format", f"Unexpected response content '{response2.content}'"


    def test_create_user_with_short_email(self):
        email = '@'
        data = {
            'password': '123',
            'username': 'learnqa',
            'firstName': 'learnqa',
            'lastName': 'learnqa',
            'email': email
        }

        response3 = requests.post("https://playground.learnqa.ru/api/user/", data=data)

        #print(response3.status_code)
        #print(response3.content)

        assert response3.status_code == 400, f"Unexpected status code '{response3.status_code}"
        assert response3.content.decode("utf-8") == f"The value of 'email' field is too short", f"Unexpected response content '{response3.content}'"

    def test_create_user_with_long_email(self):
        email = 'in_this_emai_more_than_250_symbols.............................................................................................................................................................................................................@example.com'

        data = {
            'password': '123',
            'username': 'learnqa',
            'firstName': 'learnqa',
            'lastName': 'learnqa',
            'email': email
        }

        response4 = requests.post("https://playground.learnqa.ru/api/user/", data=data)

        #print(response4.status_code)
        #print(response4.content)

        assert response4.status_code == 400, f"Unexpected status code '{response4.status_code}"
        assert response4.content.decode("utf-8") == f"The value of 'email' field is too long", f"Unexpected response content '{response3.content}'"

    @pytest.mark.parametrize('data', datas)
    def test_create_user_with_missed_param(self, data):
        data_as_dict = {
            data[0]: data[1],
            data[2]: data[3],
            data[4]: data[5],
            data[6]: data[7]
        }

        response5 = requests.post("https://playground.learnqa.ru/api/user/", data=data_as_dict)

        #print(response5.status_code)
        #print(response5.content)

        assert response5.status_code == 400, f"Unexpected status code '{response5.status_code}"
        assert response5.content.decode("utf-8") == f"The following required params are missed: {data[8]}", f"Unexpected response content '{response3.content}'"


