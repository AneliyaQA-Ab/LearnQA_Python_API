import requests

response = requests.get("https://playground.learnqa.ru/api/long_redirect", allow_redirects=True)

redirects_quantity = len(response.history) #узнаю сколько было редиректов
i = 0
for i in range(redirects_quantity):
    result = (response.history[i]).url #вывожу урл каждого редиректа
    print(result)
    i = i + 1
print(response.url) #вывожу последний урл после которого не было редиректов



