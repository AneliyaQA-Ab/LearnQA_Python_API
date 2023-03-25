import requests

response = requests.get("https://playground.learnqa.ru/api/long_redirect", allow_redirects=True)

redirects_quantity = len(response.history)
print(redirects_quantity)
print(response.url) #конечный урл




