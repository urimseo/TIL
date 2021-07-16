import requests

# naver 요청 보낼 때 필요한 것들
naver_client_id = "1ER32QEa3OPaD7JtdZXH"
naver_client_secret = "mUddv1Tdyl"
URL = "https://openapi.naver.com/v1/search/shop.json?query="

headers = {
    "X-Naver-Client-Id": naver_client_id,
    "X-Naver-Client-Secret": naver_client_secret
 }

query = 'ps5'

product = requests.get(URL+query,headers=headers).json()['items'][0]
#print(product)
product_name =product["title"]
print(product_name)
product_price = product['lprice']
print(product_price)
product_link = product['link']
print(product_link)

message =f'제품명: {product_name}\n가격: {product_price}\n링크: {product_link}'

# 텔레그램에서 최저가 불러오기
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

text = '네이버 최저가 검색결과입니다.'

message_url = f"{APP_URL}/sendMessage?chat_id={chat_id}&text={text}\n{message}"
# https://api.telegram.org/bot1862351176:AAEUnffrWdKi6Zjo-ntZO5NYI7oi4GEmG9c/sendMessage?chat_id=1876335652&text=%EB%B3%B4%EB%82%B4%EC%A7%80%EB%82%98%EC%9A%94??

requests.get(message_url)


# 1. 텔레그램 챗봇 Token
# 1862351176:AAEUnffrWdKi6Zjo-ntZO5NYI7oi4GEmG9c

# 2. 텔레그램 API URL
# https://api.telegram.org/bot<token>/METHOD_NAME