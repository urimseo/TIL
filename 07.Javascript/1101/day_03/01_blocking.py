# 1. sleep
# from time import sleep

# def sleep_3_secondes():
#     sleep(3)
#     print('잘 잤다!!')

# print('이제 자야지')
# sleep_3_secondes()
# print('학교가자!!')

# 2. requests
import requests

response = requests.get('https://jsonplaceholder.typicode.com/todos/1/')

todo = response.json()

print(todo)