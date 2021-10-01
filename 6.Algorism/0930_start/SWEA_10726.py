'''
이진수 표현
N, M -> 정수
M을 2진수로 변환
M의 N번째 비트가 1인지 아닌지 판별
'''
for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    S = ''
    for i in range(N):
        if M & (1 << i):
            S += '1'
        else:
            S += '0'

    res = 'ON'
    for i in range(len(S)-1, len(S)-N-1, -1):
        if S[i] == '0':
            res = 'OFF'
            break
    print(f'#{tc} {res}')