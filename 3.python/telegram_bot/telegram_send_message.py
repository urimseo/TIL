import requests
from requests.models import Response

# 기본 설정
TOKEN ="1862351176:AAEUnffrWdKi6Zjo-ntZO5NYI7oi4GEmG9c"
APP_URL =f"https://api.telegram.org/bot{TOKEN}"

# chat_id 가져오기
# https://api.telegram.org/bot1862351176:AAEUnffrWdKi6Zjo-ntZO5NYI7oi4GEmG9c/getUpdates
UPDATES_URL = f"{APP_URL}/getUpdates"
response = requests.get(UPDATES_URL).json()

# print(response)
# chat_id = '1876335652'

chat_id = response.get('result')[0].get('message').get('chat').get('id')
print(chat_id)

text = '파이썬으로 보낸 메세지입니다.'

message_url = f"{APP_URL}/sendMessage?chat_id={chat_id}&text={text}"
# https://api.telegram.org/bot1862351176:AAEUnffrWdKi6Zjo-ntZO5NYI7oi4GEmG9c/sendMessage?chat_id=1876335652&text=%EB%B3%B4%EB%82%B4%EC%A7%80%EB%82%98%EC%9A%94??

requests.get(message_url)



# 1. 텔레그램 챗봇 Token
# 1862351176:AAEUnffrWdKi6Zjo-ntZO5NYI7oi4GEmG9c

# 2. 텔레그램 API URL
# https://api.telegram.org/bot<token>/METHOD_NAME