'''
210901
정사각형 길이찾기 
'''
for tc in range(1, int(input())+1):
    lst = list(map(int, input().split()))
    tmp = [0] * 101

    for i in lst:
        tmp[i] += 1

    res = 0
    for k in range(1, 101):
        if tmp[k] == 1 or tmp[k] == 3:
            res = k
            break

    print('#{} {}'.format(tc, res))