import requests
import json
import time

response = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job")
parsed_response_text = response.json() #распарсила первый ответ
time_to_sleep = parsed_response_text["seconds"]
user_token = parsed_response_text["token"]

response_2 = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job") #отправляю второй запрос и сразу проверяю статус код
if response_2.status_code == 200: #проверяю, что до выполнения задачи код ответа будет 200
    time.sleep(time_to_sleep) #запуск таймаута на указанное количетсво секунд
    response_3 = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params={"token":user_token}) #третий запрос с токеном уже после таймаута
    parsed_response_3_text = response_3.json()
    status = parsed_response_3_text["status"]
    result = parsed_response_3_text["result"]
    if status != "Job is ready":
        print("Error: job is not ready after timeout")
    else:
        if len(result) >= 1:
            print('Test passed')
        else:
            print("Error: result is empty")
else:
    print('Error: Status code is not 200')

