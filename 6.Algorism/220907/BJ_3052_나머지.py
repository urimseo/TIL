'''
수 10개를 입력받은 뒤, 이를 42로 나눈 나머지를 구한다. 그 다음 서로 다른 값이 몇 개 있는지 출력
'''

dict = {}

for i in range(10):
    r = int(input()) % 42
    if r in dict :
        dict[r] += 1
    else:
        dict[r] = 1

print(len(dict.keys()))



