import requests
from lib.base_case import BaseCase
from lib.assertions import Assertions
from datetime import datetime

class TestUserDelete(BaseCase):


    def test_delete_just_created_user(self):
        # REGISTER
        register_data = self.prepare_registration_data()
        response1 = requests.post("https://playground.learnqa.ru/api/user", data=register_data)

        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        email = register_data['email']
        firstName = register_data['firstName']
        password =  register_data['password']
        user_id = self.get_json_value(response1, "id")

        #LOGIN

        login_data = {
            'email': email,
            'password': password
        }

        response2 = requests.post("https://playground.learnqa.ru/api/user/login", data=login_data)

        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_header(response2, "x-csrf-token")


        #DELETE

        new_name = "Changed Name"

        response3  = requests.delete(
            f"https://playground.learnqa.ru/api/user/{user_id}",
            headers={"x-csrf-token":token},
            cookies={"auth_sid":auth_sid},
        )

        #print(response3)
        #print(response3.content)

        Assertions.assert_code_status(response3, 200)


        #GET
        response4 = requests.get(f"https://playground.learnqa.ru/api/user/{user_id}",
                                  headers={"x-csrf-token": token},
                                  cookies={"auth_sid": auth_sid}
                                  )


        #print(response4)
        #print(response4.content)

        Assertions.assert_code_status(response4, 404)

    def test_delete_user_disabled_for_edit(self):

        # LOGIN

        login_data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }

        response5 = requests.post("https://playground.learnqa.ru/api/user/login", data=login_data)

        auth_sid = self.get_cookie(response5, "auth_sid")
        token = self.get_header(response5, "x-csrf-token")

        # DELETE


        response6 = requests.delete(
            f"https://playground.learnqa.ru/api/user/2",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid},
        )

        #print(response6)
        #print(response6.content)

        Assertions.assert_code_status(response6, 400)

    def test_delete_other_user(self):
        # REGISTER
        register_data = self.prepare_registration_data()
        response7 = requests.post("https://playground.learnqa.ru/api/user", data=register_data)

        Assertions.assert_code_status(response7, 200)
        Assertions.assert_json_has_key(response7, "id")

        user_id = self.get_json_value(response7, "id")


        # REGISTER_OTHER_USER
        new_register_data = self.prepare_registration_data()
        response10 = requests.post("https://playground.learnqa.ru/api/user", data=new_register_data)

        Assertions.assert_code_status(response10, 200)
        Assertions.assert_json_has_key(response10, "id")

        email = register_data['email']
        password = register_data['password']
        other_user_id = self.get_json_value(response10, "id")


        #LOGIN_BY_OTHER_USER

        login_data = {
            'email': email,
            'password': password
        }

        response11 = requests.post("https://playground.learnqa.ru/api/user/login", data=login_data)

        other_user_auth_sid = self.get_cookie(response11, "auth_sid")
        other_user_token = self.get_header(response11, "x-csrf-token")


        #DELETE__BY_OTHER_USER

        response12  = requests.delete(
            f"https://playground.learnqa.ru/api/user/{user_id}",
            headers={"x-csrf-token":other_user_token},
            cookies={"auth_sid":other_user_auth_sid},
        )

        #print(user_id)
        #print(other_user_id)
        #print(response12)
        #print(response12.content)

        Assertions.assert_code_status(response12, 200) #почему тут 200?



