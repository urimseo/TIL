'''
이진수2


N = 0.625
0.101 (이진수)
= 1*2-1 + 0*2-2 + 1*2-3
= 0.5 + 0 + 0.125
= 0.625
'''


for tc in range(1, int(input())+1):
    a = float(input())
    x = 1
    res = ''
    while x != 0:
        tmp = (a - 1/(2 ** x))
        if (a - 1/(2 ** x)) > 0:
            res += '1'
            a = a - 1/(2 ** x)
        elif (a - 1/(2 ** x)) < 0:
            res += '0'
        else:
            res += '1'
            break
        x += 1
    if len(res) <= 12:
        print(f'#{tc} {res}')
    else:
        print(f'#{tc} overflow')
