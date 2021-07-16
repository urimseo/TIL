import requests #라이브러리 가져오기
from bs4 import BeautifulSoup

url ='https://finance.naver.com/sise/'
response = requests.get(url).text #요청 보내고 받은 응답 text로 변환
data = BeautifulSoup(response,"html.parser") #응답으로 받은 걸 처리하기 쉽게 가공(parsing)
kospi = data.select_one('#KOSPI_now')
kosdaq = data.select_one('#KOSDAQ_now')
# popularlist = data.select_one('#popularItemList > li:nth-child({i}) > a')

result = kospi.text
result2 = kosdaq.text


print(f'현재 코스피 지수는 {result}이며, 코스닥 지수는 {result2}입니다.')
print(f'TOP 10 인기 종목은: ')

for i in range(1,11):
    popitem = data.select_one(f"#popularItemList > li:nth-child({i}) > a")
    print(popitem.text)


