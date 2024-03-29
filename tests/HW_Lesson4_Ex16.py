from logging import CRITICAL

import requests
from lib.base_case import BaseCase
from lib.assertions import Assertions
from lib.my_requests import MyRequests
import allure

@allure.epic("Authorization cases")
@allure.link(name = "Документация API", url = "https://playground.learnqa.ru/api/map")
@allure.issue('https://jira.kvantera.io/browse/QA-81', 'Пройти курс "Автоматизация API на python')


class TestUserGet(BaseCase):
    @allure.description("This test  authorize user w/o auth")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_get_user_details_not_auth(self):
         response = MyRequests.get("/user/2") # захардкодили id  = 2

         Assertions.assert_json_has_key(response, "username")
         Assertions.assert_json_has_not_key(response, "email")
         Assertions.assert_json_has_not_key(response, "firstName")
         Assertions.assert_json_has_not_key(response, "lastName")

    @allure.description("This test  authorize as same user")
    def test_get_user_details_auth_as_same_user(self):
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }


        response1 = MyRequests.post("/user/login", data=data)

        auth_sid = self.get_cookie(response1, "auth_sid")
        token = self.get_header(response1, "x-csrf-token")
        user_id_from_auth_method = self.get_json_value(response1, "user_id")
        #print(response1.content)


        response2 = MyRequests.get(
            f"/user/{user_id_from_auth_method}",
            headers={"x-csrf-token":token},
            cookies= {"auth_sid":auth_sid}
        )

        expected_fields = ["username", "email", "firstName","lastName"]
        Assertions.assert_json_has_keys(response2, expected_fields)

    @allure.description("This test  authorize as same user")
    def test_get_user_details_auth_as_not_same_user(self):
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }


        response1 = MyRequests.post("/user/login", data=data)

        auth_sid = self.get_cookie(response1, "auth_sid")
        token = self.get_header(response1, "x-csrf-token")
        #print(response1.content)


        response2 = MyRequests.get(
            f"/user/1", #захардкодили, для логина и пароля выше id = 2
            headers={"x-csrf-token":token},
            cookies= {"auth_sid":auth_sid}
        )

        Assertions.assert_json_has_key(response2, "username")

        expected_fields = ["email", "firstName", "lastName"]
        Assertions.assert_json_has_not_keys(response2, expected_fields)
