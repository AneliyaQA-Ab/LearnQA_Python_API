import requests

print(f"Отправляю запрос c пустым payload")
response = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params='')
print(f" Для параметра GET без payload ответ сервера {response}, {response.text}")  # вывожу ответ для запроса без payloaf
print(f"===================")

print(f"Запускаю цикл для запроса не из спика  HEAD")
payload_head = {"method": "HEAD"}
response = requests.head("https://playground.learnqa.ru/ajax/api/compare_query_type", params=payload_head)
print(f"HEAD https://playground.learnqa.ru/ajax/api/compare_query_type, params = HEAD") #вывожу метод и запрос
print(f"{response}, {response.text}")
print(f"===================")


meth = ["GET", "POST", "PUT", "DELETE"] #определила список доступных методов
print(f"Запускаю цикл для GET")
for i in meth: #цикл для GET
    print(f"GET https://playground.learnqa.ru/ajax/api/compare_query_type, params = {i}") #вывожу метод и запрос
    payload = {"method": str(i)}
    response = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params=payload)
    print(f"{response}, {response.text}")  #вывожу ответ
print(f"===================") #для читабельности вывода

print(f"Запускаю цикл для POST")
for i in meth: #цикл для POST
    print(f"POST https://playground.learnqa.ru/ajax/api/compare_query_type, params = {i}") #вывожу метод и запрос
    payload = {"method": str(i)}
    response = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", data=payload)
    print(f"{response}, {response.text}")  #вывожу ответ
print(f"===================")

print(f"Запускаю цикл для PUT")
for i in meth: #цикл для PUT
    print(f"PUT https://playground.learnqa.ru/ajax/api/compare_query_type, params = {i}") #вывожу метод и запрос
    payload = {"method": str(i)}
    response = requests.put("https://playground.learnqa.ru/ajax/api/compare_query_type", data=payload)
    print(f"{response}, {response.text}")  #вывожу ответ
print(f"===================")

print(f"Запускаю цикл для DELETE")
for i in meth: #цикл для DELETE
    print(f"DELETE https://playground.learnqa.ru/ajax/api/compare_query_type, params = {i}") #вывожу метод и запрос
    payload = {"method": str(i)}
    response = requests.delete("https://playground.learnqa.ru/ajax/api/compare_query_type", data=payload)
    print(f"{response}, {response.text}")  #вывожу ответ
print(f"===================")



