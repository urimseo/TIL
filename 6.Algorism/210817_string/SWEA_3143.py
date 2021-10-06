'''
가장 빠른 문자열 타이핑
A = 문자열
B = 단축어
'''
T = int(input())
for tc in range(1, T+1):
    A, B = input().split()
    a = len(A)
    b = len(B)

    res = 0 # 총 개수
    for i in range(a):
        if res != 0:
            i = i+(b*res)-res
        cnt = 0  # 개수
        for j in range(b):
            if i < a and A[i] == B[j]:
                i += 1
                cnt += 1
                if cnt == len(B):
                    res += 1

    total = a - (b-1)*res
    print(f'#{tc} {total}')



