

import pytest #чтобы использовать parametrize
import requests

class TestUserAgent:
    names = [
                [('Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30'), ('Mobile'), ('No'), ('Android')],
        [('Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/91.0.4472.77 Mobile/15E148 Safari/604.1'), ('Mobile'), ('Chrome'), ('iOS')],
        [('Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'), ('Googlebot'), ('Unknown'), ('Unknown')],
        [('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.100.0'), ('Web'), ('Chrome'), ('No')],
        [('Mozilla/5.0 (iPad; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'), ('Mobile'), ('No'), ('iPhone')]

    ]
    @pytest.mark.parametrize('name', names)
    def test_user_agent(self, name):
        url = "https://playground.learnqa.ru/ajax/api/user_agent_check"
        headers = {"User-Agent": name[0]}

        response = requests.get(url, headers=headers)

        #print(name)

        #print(response.json())
        current_key = 'platform'
        сurrent_value = response.json()[current_key]
        assert сurrent_value == name[1], f"Value of key 'platform' is not correct, current value is {сurrent_value}, User Agent is {name[0]}"
        current_key_2 = 'browser'
        сurrent_value = response.json()[current_key_2]
        assert сurrent_value == name[2], f"Value of key 'browser' is not correct, current value is {сurrent_value}, User Agent is {name[0]}"
        current_key_3 = 'device'
        сurrent_value = response.json()[current_key_3]
        assert сurrent_value == name[3], f"Value of key 'device' is not correct, current value is {сurrent_value}, User Agent is {name[0]}"



