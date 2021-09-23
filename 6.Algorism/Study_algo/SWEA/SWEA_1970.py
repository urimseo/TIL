for tc in range(1, int(input())+1):
    change = int(input())
    money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    res = [0] * len(money)
    while change != 0:
        for m in range(len(money)):
            if change - money[m] >= 0:
                change -= money[m]
                res[m] += 1
                break
        if change < 10:
            change = 0
            break
    print('#{}'.format(tc))
    print(*res)

