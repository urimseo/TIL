'''
0000000111100000011000000111100110000110000111100111100111111001100111
'''

for tc in range(1, int(input())+1):
    lst = list(map(int, input()))
    # 7개씩 잘라 b6 ~ b0으로 사용
    ans = []
    dec = 0
    for i in range(70):
        # i % 7 0~6을 반복해서 만드는 연산
        # 1<<i i번 비트가 1인값, 2의 i제곱수
        j = 6 - i % 7
        dec += lst[i] * (1 << j)
        if j == 0:
            ans.append(dec)
            dec = 0
    print(f'#{tc}', *ans)