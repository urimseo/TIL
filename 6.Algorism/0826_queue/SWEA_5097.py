
for tc in range(1, int(input())+1) :
    n, m = map(int, input().split())
    lst = list(map(int, input().split()))
    tmp = 0
    for i in range(m):
        tmp = lst.pop(0)
        lst.append(tmp)
    print(f'#{tc} {lst[0]}')