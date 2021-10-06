# 뒤에서부터 찾기....
# 맨 뒤가 최고가라고 생각
# 앞으로 오면서 작으면 차익 누적

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    price = list(map(int, input().split()))

    res = 0
    maxprice = price[-1]
    for i in range(n-1, -1, -1):
        if price[i] > maxprice:
            maxprice = price[i]
        else:
            res += maxprice - price[i]
    print(f'#{tc} {res}')