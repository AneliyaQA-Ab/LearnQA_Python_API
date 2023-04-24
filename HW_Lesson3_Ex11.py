import requests
class TestCookie:
    def test_cookie(self):
        url = "https://playground.learnqa.ru/api/homework_cookie"

        response = requests.get(url)

        assert len(response.cookies) != 0, "No cookies in response" #проверка что кука возвращается

        cookie_value = response.cookies['HomeWork']
        expected_value = ('hw_value')

        assert cookie_value == expected_value, "Wrong cookie value" #проверка на нужное значение





#