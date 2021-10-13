'''
정식이의 은행 업무

2진수, 3진수 한자리씩 잘못 기억하고 있다.
2진수 한자리씩 바꾼 값 저장 -> 3진수 바꾸면서 일치하는것 찾으면 됨

1010 -> 1011, 1000, 1110, 0010
        13,    8,   14,    2
# 토글
1010 ^ 0001 , 1010 ^ 0010 , 1010 ^ 0100, 1010 ^ 1000

# 2진수 -> 10 진수 변경하는 법
tmp = tmp *2 + i(자릿수)

enumerate (리스트)-> 인덱스, 값
tmp += i * (n진수 ** 몇승)

# 하나의 비트만 바꾸어 저장


212 -> 210, 211, 202, 222, 012, 112
                                 14

'''
# 10진수로 바꾸기
def change_e(lst, x):
    res = 0
    for k in range(len(lst)-1, -1, -1):
        idx = int(lst[len(lst)-k-1])
        if idx:
            res += idx*x**k
    return res

for tc in range(1, int(input())+1):
    ejin = list(input())
    sjin = list(input())
    elst = []
    # 2진수의 수를 하나씩 변환
    for i in range(len(ejin)):
        if ejin[i] == '1':
            tmp = ejin[::]
            tmp[i] = '0'
            # elst.append(int((''.join(tmp)), 2))
            elst.append(change_e(tmp, 2)) # 10 진수를 바꾼 수를 리스트에 저장
        elif ejin[i] == '0':
            tmp = ejin[::]
            tmp[i] = '1'
            # elst.append(int((''.join(tmp)), 2))
            elst.append(change_e(tmp, 2))

    # 3진수 바꾸기
    sj = ['0', '1', '2']
    flag = 0   # tc가 여러개 있기 때문에 flag를 초기화 해야 다음 tc에서 flag가 0인 상태로 시작한다. 그렇지 않으면, flag 가 1 인 상태로 들어가서 바로 break 되버림!! 주의하기!!!
    for j in range(len(sjin)):
        for s in range(3):
            if sjin[j] == sj[s]: continue
            tmp2 = sjin[::]
            tmp2[j] = sj[s]
            # fix = int((''.join(tmp2)), 3)
            fix = change_e(tmp2, 3)
            if fix in elst:
                flag = 1
                break
        if flag:
            break
    print(f'#{tc} {fix}')





