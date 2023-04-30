import requests
class TestHeader:
    def test_header(self):
        url = "https://playground.learnqa.ru/api/homework_header"
        name = 'x-secret-homework-header'

        response = requests.get(url)
        headers = response.headers

        #print(headers)
        assert name in headers, f"Response headers  doesn't have key '{name}'" #проверка что в хедерах есть нужный ключ

        header_value = response.headers[name]
        expected_value = ('Some secret value')

        assert header_value == expected_value, "Wrong header value" #проверка на нужное значение