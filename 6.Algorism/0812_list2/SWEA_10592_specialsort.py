'''
선택정렬로 다시 풀기!

'''
















'''
T = int(input())
for tc in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    res = []
    for a in range(5):
        maxV = 0
        minV = 101
        for i in arr:
            if maxV < i:
                maxV = i
            if minV > i:
                minV = i
        res.extend([maxV, minV])
        arr.remove(maxV)
        arr.remove(minV)

    tmp = ' '.join(map(str,res))
    print(f'#{tc+1} {tmp}')
    # print(' '.join(map(str, res[:10])))
'''
