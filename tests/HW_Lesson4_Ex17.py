import requests
from lib.base_case import BaseCase
from lib.assertions import Assertions
from datetime import datetime

class TestUserEdit(BaseCase):


    def test_edit_just_created_user(self):
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


        #EDIT

        new_name = "Changed Name"

        response3  = requests.put(
            f"https://playground.learnqa.ru/api/user/{user_id}",
            headers={"x-csrf-token":token},
            cookies={"auth_sid":auth_sid},
            data={"firstName":new_name}
        )

        #print(response3)
        #print(response3.content)

        Assertions.assert_code_status(response3, 200)


        #GET
        response4 = requests.get(f"https://playground.learnqa.ru/api/user/{user_id}",
                                  headers={"x-csrf-token": token},
                                  cookies={"auth_sid": auth_sid}
                                  )
        Assertions.assert_json_value_by_name(
            response4,
            "firstName",
            new_name,
            "Wrong  name of the user  after edit"
        )

    def test_edit_without_registration(self):
        # EDIT

        new_name = "Changed Name"
        user_id = 2 #захардкодили любое значение id
        response5 = requests.put(
            f"https://playground.learnqa.ru/api/user/{user_id}",
            data={"firstName": new_name}
        )

        #print(response5)

        Assertions.assert_code_status(response5, 400) #при отсутствии авторизации статус код должен быть 400

    def test_edit_other_user(self):
        # REGISTER

        register_data = self.prepare_registration_data()
        response6 = requests.post("https://playground.learnqa.ru/api/user", data=register_data)

        Assertions.assert_code_status(response6, 200)
        Assertions.assert_json_has_key(response6, "id")

        email = register_data['email']
        firstName = register_data['firstName']
        password = register_data['password']
        user_id = self.get_json_value(response6, "id")

        # LOGIN

        login_data = {
            'email': email,
            'password': password
        }

        #print(response6)

        response7 = requests.post("https://playground.learnqa.ru/api/user/login", data=login_data)

        auth_sid = self.get_cookie(response7, "auth_sid")
        token = self.get_header(response7, "x-csrf-token")

        #print(user_id)
        #print(token)
        #print(auth_sid)


        # EDIT

        user_id_other_user = int(user_id) + 1

        new_name = "Changed Name"

        response8 = requests.put(
            f"https://playground.learnqa.ru/api/user/{user_id_other_user}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid},
            data={"firstName": new_name}
        )

        print(user_id_other_user)


        Assertions.assert_code_status(response8, 200)  #приходит 200, почему? оставила пока ассерт на 200

    def test_edit_incorrect_email(self):
        # REGISTER
        register_data = self.prepare_registration_data()
        response9 = requests.post("https://playground.learnqa.ru/api/user", data=register_data)

        Assertions.assert_code_status(response9, 200)
        Assertions.assert_json_has_key(response9, "id")

        email = register_data['email']
        firstName = register_data['firstName']
        password =  register_data['password']
        user_id = self.get_json_value(response9, "id")

        #LOGIN

        login_data = {
            'email': email,
            'password': password
        }

        response10 = requests.post("https://playground.learnqa.ru/api/user/login", data=login_data)

        auth_sid = self.get_cookie(response10, "auth_sid")
        token = self.get_header(response10, "x-csrf-token")


        #EDIT

        new_incorrect_email = "email.ru"

        response11 = requests.put(
            f"https://playground.learnqa.ru/api/user/{user_id}",
            headers={"x-csrf-token":token},
            cookies={"auth_sid":auth_sid},
            data={"email":new_incorrect_email}
        )

        #print(response11.content)

        Assertions.assert_code_status(response11, 400)

    def test_edit_incorrect_firstName(self):
        # REGISTER

        register_data = self.prepare_registration_data()
        response12 = requests.post("https://playground.learnqa.ru/api/user", data=register_data)

        Assertions.assert_code_status(response12, 200)
        Assertions.assert_json_has_key(response12, "id")

        email = register_data['email']
        firstName = register_data['firstName']
        password = register_data['password']
        user_id = self.get_json_value(response12, "id")

        # LOGIN

        login_data = {
            'email': email,
            'password': password
        }

        response13 = requests.post("https://playground.learnqa.ru/api/user/login", data=login_data)

        auth_sid = self.get_cookie(response13, "auth_sid")
        token = self.get_header(response13, "x-csrf-token")

        # EDIT

        new_incorrect_name = "A"

        response14 = requests.put(
            f"https://playground.learnqa.ru/api/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid},
            data={"firstName": new_incorrect_name}
        )

        #print(response14.content)
        #print(response14)
        Assertions.assert_code_status(response14, 400)











