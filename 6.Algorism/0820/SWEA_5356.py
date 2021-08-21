'''
의석이의 세로로 말해요
AABCDD
afzz
09121
a8EWg6
P5h3kx

#1 Aa0aPAf985Bz1EhCz2W3D1gkD6x
[['A', 'A', 'B', 'C', 'D', 'D'],
 ['a', 'f', 'z', 'z'],
 ['0', '9', '1', '2', '1'],
 ['a', '8', 'E', 'W', 'g', '6'],
 ['P', '5', 'h', '3', 'k', 'x']]
'''
T = int(input())
for tc in range(1, T+1):
    text = [list(input()) for _ in range(5)]
    maxlen = 0
    # 최대 길이 찾기
    for i in text:
        if maxlen < len(i):
            maxlen= len(i)
    #최대길이보다 작은만큼 공백 더하기
    for i in text:
        if len(i) < maxlen:
            cnt = maxlen - len(i)
            for j in range(cnt):
                i.append('')
    # 90도 회전
    textv = list(zip(*text[::-1]))
    # 역방향이라 반대로 출력
    print(f'#{tc}', end =' ')
    for i in textv:
        for j in range(len(i)-1, -1, -1):
            print(i[j], end='')
    print()

