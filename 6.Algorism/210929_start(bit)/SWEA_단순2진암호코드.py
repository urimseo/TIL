'''
단순 2진 암호코드
모든 암호코드는 8개의 숫자로 구성되어 있다.
암호코드의 가로길이 (N)
암호코드의 세로길이 (M)

각각의 코드를 확인하는데 ( 한 코드는 56개입력, /8 * 8/, 세로길이는 암호의 개수)

0. 코드의 시작점과 끝을 찾아야한다.
a. 암호의 맨 마지막 수는 무조건 1 -> 뒤에서부터 암호의 끝점을 찾기
b. 암호의 시작점까지 끊은 뒤에, 7씩 슬라이싱 해서 확인하면서

## (홀수 자리의 합 x 3) + 짝수 자리의 합 + 검증 코드 % 10 == 0 이면 정상 코드
1. 8개 입력 끊어서 2진수 -> 딕셔너리에 0~9까지의 값 저장하여 비교해서  key-value 로 가져온다.
2. 빈 배열 에서 정상 암호 검증하기


정상 암호인 경우 -> tmp = 각 자리수의 합
비정상 암호 -> tmp = 0
-> 모든 암호의 각 자리수의 합을 더함 (sum(res)) -> 빈 배열(res)에다가 tmp값을 append



'''

c_num = {'0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3, '0100011': 4, '0110001': 5, '0101111': 6, '0111011': 7, '0110111': 8, '0001011': 9}
for tc in range(1, int(input())+1):
    n, m = map(int, input().split())
    lst = [input() for _ in range(n)]
    code = '' # 암호가 있는 줄만 들어가게 된다.
    for k in lst:
        for i in range(len(k)-1, 55, -1): # 한줄씩 찾는데 역순으로
            if k[i] == '1': # 1을 발견하면 끝수니까.
                code = k[i-55:i+1]
                break
        if code:
            break
    numlst = [] # 딕셔너리값과 비교하여 숫자 일치시키기
    for i in range(8):
        num = code[i*7 : i*7+7]
        numlst.append(c_num[num])

    # 코드 유효성 검증
    res = 0
    for j in range(8):
        if j % 2 == 1:  # 홀수자리합 / 검증코드
            res += numlst[j]
        else:           # 짝수
            res += numlst[j] * 3

    if res % 10 == 0:
        print(f'#{tc} {sum(numlst)}')
    else:
        print(f'#{tc} 0')



'''

while문으로 코드를 돌릴 경우!

a = 0
while a < 56:
    # code 7개씩 슬라이싱 
    key = code[a : a +7] # 0 ~6
    lst.append(c_num[num])
    a += 7
'''