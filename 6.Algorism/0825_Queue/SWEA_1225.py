'''
암호생성기
'''
for t in range(10):
    tc = int(input())
    lst = list(map(int, input().split()))
    q = [] # 큐 그냥 계속 누적시킬거야..
    first = -1
    while lst[-1] != 0:
        for i in range(1, 6):
            first = lst.pop(0)
            lst.append(first-i)
            if lst[-1] <= 0:
                lst[-1] = 0
                break
    print(f'#{tc}', end=' ')
    print(*lst)

