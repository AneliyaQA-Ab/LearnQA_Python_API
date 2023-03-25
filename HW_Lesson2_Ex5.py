import json

first_string_as_json_format = '{"messages":[{"message":"This is the first message","timestamp":"2021-06-04 16:40:53"},{"message":"And this is a second message","timestamp":"2021-06-04 16:41:01"}]}'
obj = json.loads(first_string_as_json_format) #перевожу в словарь
key = "messages"

if key in obj:
    messages = obj[key] #забираю все значения по ключу messages
    second_message_as_obj = messages[1] #забираю json второго сообщения
    print(second_message_as_obj)
    key_2 = "message" #забираю по ключу только значение второго сообщения
    if key_2 in second_message_as_obj:
        print(second_message_as_obj[key_2])
    else:
        print(f"Ключа {key_2} в JSON net")

else:
    print(f"Ключа {key} в JSON net")


